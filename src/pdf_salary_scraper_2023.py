# -*- coding: utf-8 -*-
import re

import pandas as pd
from PyPDF2 import PdfReader

from __init__ import provinces, regions


def extract_salary_data(pdf_path="data/pdf/2023_salary_guide.pdf"):
    # Creating a pdf reader object
    reader = PdfReader(pdf_path)

    # Initializing data dictionary
    data = {
        "province": [],
        "region": [],
        "job": [],
        "entry": [],
        "mid": [],
        "senior": [],
    }

    # Extracting data from each page
    for page in reader.pages:
        text = page.extract_text().lower()

        current_region = ""
        current_province = ""

        for line in text.splitlines():
            # Find the province
            for province in provinces:
                if province in text.lower():
                    current_province = province  # Save the province that was found
                    break  # Exit the loop once a province is found
            for region in regions:
                if region in text.lower():
                    current_region = region
                    break

            # Extract job title and salary range
            if "-" in line.lower():
                # Administrative assistant43.6 - 56.449.9 - 61.355.2 - 66.7
                # Administrative manager65.2 - 74.371.1 - 81.978.7 - 94.6
                regex = r"^(\D+)(.*)$"

                # Extract job title
                match = re.match(regex, line)
                if match is None:
                    continue
                job_title = match[2].strip()

                # Split remaining numbers
                numbers = match[2]

                # 14.25 - 18.0 16.0 - 21.0 18.0 -21.0
                pattern = r"(\d+\.\d+)\s*-\s*(\d+\.\d+)"

                # Find all matches of the pattern in the line
                numbers = re.findall(pattern, numbers)

                # Split numbers into 3 groups or 4 groups(finance department)
                if len(numbers) == 3:
                    entry_range = numbers[0][0] + "-" + numbers[1][1]
                    mid_range = numbers[1][0] + "-" + numbers[1][1]
                    senior_range = numbers[2][0] + "-" + numbers[2][1]
                elif len(numbers) == 4:
                    continue

                # Append extracted data to dictionary
                data["job"].append(job_title)
                data["entry"].append(entry_range)
                data["mid"].append(mid_range.strip())
                data["senior"].append(senior_range.strip())
                data["province"].append(current_province)
                data["region"].append(current_region)

    return data


if __name__ == "__main__":
    # save data to pickle file
    data = extract_salary_data()
    output_file = "data/pickle/salary_guide_2023.pkl"
    pd.to_pickle(data, output_file)
    df = pd.DataFrame(data)
    print(df.head())
