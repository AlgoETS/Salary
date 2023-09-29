from PyPDF2 import PdfReader
import re
import pandas as pd
from __init__ import provinces, regions  # Replace with your actual import

def extract_salary_data(pdf_path, year):
    reader = PdfReader(pdf_path)
    data = {'province': [], 'region': [], 'job': [], 'entry': [], 'mid': [], 'senior': []}
    current_region = ""
    current_province = ""

    for page_number, page in enumerate(reader.pages, start=1):
        print(f"Processing page {page_number}")
        text = page.extract_text().lower()

        current_province = next((province for province in provinces if province in text), "Missing Province")
        current_region = next((region for region in regions if region in text), "Missing Region")

        for line in text.splitlines():
            if f"guide salarial {year}" in line or f"{year} salary guide" in line:
                pattern = r"\d{4}\s\S+\s\S+\s+\|\d+"
                line = re.sub(pattern, "", line)

            if "-" in line:
                regex = r"^([a-zA-Z\s\-\&]+)([\d\.\-\,\s]+)$"
                try:
                    if match := re.match(regex, line.strip()):
                        job_title = match[1].strip()
                        numbers = match[2]
                        pattern = r"(\d+\.\d+)\s*-\s*(\d+\.\d+)"
                        numbers = re.findall(pattern, numbers)

                        if len(numbers) == 3:
                            entry_range, mid_range, senior_range = [f"{start}-{end}" for start, end in numbers]
                            data['job'].append(job_title)
                            data['entry'].append(entry_range)
                            data['mid'].append(mid_range)
                            data['senior'].append(senior_range)
                            data['province'].append(current_province)
                            data['region'].append(current_region)
                        else:
                            print(f"No match found on this line: {line}")

                except Exception as e:
                    print(f"An error occurred on page {page_number} on this line: {line}")
                    print(f"Error details: {e}")

    output_file = f"data/pickle/salary_guide_{year}.pkl"
    pd.to_pickle(data, output_file)
    df = pd.DataFrame(data)
    print(df.head())

# Usage
extract_salary_data("data/pdf/2023_salary_guide.pdf", 2023)
extract_salary_data("data/pdf/2024_salary_guide.pdf", 2024)
