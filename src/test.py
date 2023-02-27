# -*- coding: utf-8 -*-
import unittest
from pathlib import Path

from bs4 import BeautifulSoup

from pdf import font_tags, fonts, headers_para
from src.pdf_salary_scraper import extract_salary_data
from src.stackoverflow_scraper import (
    extract_salary_data as extract_salary_data_stackoverflow,
)


def test_headers_para():
    # Open the PDF file
    doc = fitz.open("./data/2023 Salary Guide _PDF.pdf")

    # Define the expected output
    expected_output = [
        "<h1>Salary Guide 2023|</h1>",
        "<h2>Introduction|</h2>",
        "<p>Welcome to the Robert Half Salary Guide 2023, your definitive guide to salaries for a variety of industries and job functions across Canada. This year’s guide includes salary information for more than 290 positions. Use the Salary Guide to gain insights into what drives compensation in today’s job market and to help navigate the many complexities associated with attracting and retaining top talent. Whether you’re researching a job offer or looking for salary trends, this guide has the information you need. |</p>",
        "<h2>How to Use the Salary Guide|</h2>",
        "<p>The Robert Half Salary Guide is divided into four sections. |</p>",
        "<h3>Industry Overview|</h3>",
        "<p>In-depth analysis of the latest trends in your industry, including job descriptions, hiring and salary trends, and much more. |</p>",
        "<h3>Position Descriptions|</h3>",
        "<p>Insight into the day-to-day responsibilities and requirements for each position, as well as a detailed look at the salary ranges associated with each role. |</p>",
        "<h3>Regional Salary Data|</h3>",
        "<p>Salary information for specific markets in Canada, so you can compare compensation in different regions. |</p>",
        "<h3>Custom Salary Reports|</h3>",
        "<p>Access to custom salary reports, created based on your company’s unique needs and requirements. |</p>",
        "<h2>Contact Us|</h2>",
        "<p>Get in touch with us if you have any questions about the Salary Guide, or if you would like to discuss your hiring needs with one of our staffing experts. |</p>",
        "<p>Visit roberthalf.ca to learn more. |</p>",
    ]

    # Get the actual output
    font_counts, styles = fonts(doc, granularity=False)
    size_tag = font_tags(font_counts, styles)
    actual_output = headers_para(doc, size_tag)

    # Assert that the actual output matches the expected output
    assert actual_output == expected_output


def test_font_tags():
    font_counts = [(10.0, 100), (12.0, 50), (14.0, 30), (16.0, 20)]
    styles = {
        10.0: {"size": 10, "font": "Arial", "bold": True},
        12.0: {"size": 12, "font": "Arial", "italic": True},
        14.0: {"size": 14, "font": "Times New Roman", "bold": True},
        16.0: {"size": 16, "font": "Times New Roman"},
    }
    expected_result = {10.0: "<p>", 12.0: "<h1>", 14.0: "<h2>", 16.0: "<s1>"}
    assert font_tags(font_counts, styles) == expected_result


class TestProcessPDF(unittest.TestCase):
    def setUp(self):
        self.pdf_file = Path("data/2023 Salary Guide _PDF.pdf")
        self.expected_columns = ["province", "region", "job", "entry", "mid", "senior"]

    def test_process_pdf_output_columns(self):
        # Call the function to process the PDF
        data = extract_salary_data(self.pdf_file)

        # Check that the data has the expected columns
        self.assertEqual(list(data.columns), self.expected_columns)

    def test_process_pdf_output_data(self):
        # Call the function to process the PDF
        data = extract_salary_data(self.pdf_file)

        # Check that the data has some expected values
        expected_values = {
            "job": ["director of operations", "administrative assistant"],
            "entry": ["110.0 -140.0", "43.6 - 56.4"],
            "mid": ["186.0 -190.0", "49.9 - 61.3"],
            "senior": ["210.0 -230.0", "55.2 - 66.7"],
        }
        for column in self.expected_columns:
            self.assertListEqual(
                list(data[column].head(2)), expected_values.get(column, [])
            )


class TestScrapeSalaryData(unittest.TestCase):
    def test_scrape_salary_data(self):
        # create a sample HTML table to test with
        html = """
            <table>
                <tr>
                    <th>Developer Type</th>
                    <th>Median Salary</th>
                    <th>Bottom Quartile Salary</th>
                    <th>Top Quartile Salary</th>
                </tr>
                <tr>
                    <td>Web Developer</td>
                    <td>$75,000</td>
                    <td>$60,000</td>
                    <td>$95,000</td>
                </tr>
                <tr>
                    <td>Data Scientist</td>
                    <td>$110,000</td>
                    <td>$85,000</td>
                    <td>$140,000</td>
                </tr>
            </table>
        """

        # parse the HTML and extract the salary data
        soup = BeautifulSoup(html, "html.parser")
        salary_data = extract_salary_data_stackoverflow(soup)

        # define the expected output
        expected_output = {
            "Web Developer": {
                "median_salary": "$75,000",
                "bottom_quartile_salary": "$60,000",
                "top_quartile_salary": "$95,000",
            },
            "Data Scientist": {
                "median_salary": "$110,000",
                "bottom_quartile_salary": "$85,000",
                "top_quartile_salary": "$140,000",
            },
        }

        # assert that the output matches the expected output
        self.assertEqual(salary_data, expected_output)


if __name__ == "__main__":
    unittest.main()
