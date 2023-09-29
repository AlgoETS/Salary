
import re
import pandas as pd
from PyPDF2 import PdfReader

from __init__ import provinces, regions

def extract_salary_data(pdf_path="data/pdf/2024_salary_guide.pdf"):
    reader = PdfReader(pdf_path)
    data = {
        "province": [],
        "region": [],
        "job": [],
        "entry": [],
        "mid": [],
        "senior": [],
    }

    for page in reader.pages:
        text = page.extract_text().lower()

        current_province = next((province for province in provinces if province in text), "Missing Province")
        current_region = next((region for region in regions if region in text), "Missing Region")
        # print(f"Current province: {current_province}, current region: {current_region}")  # Debugging line

        for line in text.splitlines():
            # print(f"Current line: {line}")  # Debugging line
            if "-" in line:
                regex = r"^([\D\·]+)([\d\.\s\-\,]+)$"
                # print(re.match(regex, line))  # Debugging line
                if match := re.match(regex, line):
                    job_title, numbers = match.groups()
                    # print(f"Debug: job_title = {job_title}")  # Debugging line
                    # print(f"Debug: numbers = {numbers}")  # Debugging line
                    pattern = r"(\d+,\d+)\s*-\s*(\d+,\d+)"
                    number_ranges = re.findall(pattern, numbers)
                    # print(f"Debug: numbers = {numbers}")  # Debugging line
                    # print(f"Debug: number_ranges = {number_ranges}")  # Debugging line

                    if len(number_ranges) == 3:
                        junior_range, interm_range, senior_range = [f"{start}-{end}" for start, end in number_ranges]

                        print(f"Captured data: {job_title}, {junior_range}, {interm_range}, {senior_range}")  # Debugging line

                        data["job"].append(job_title.strip())
                        data["junior"].append(junior_range)
                        data["interm."].append(interm_range)
                        data["sénior"].append(senior_range)
                        data["province"].append(current_province)
                        data["region"].append(current_region)

    return data


if __name__ == "__main__":
    data = extract_salary_data(pdf_path="data/pdf/2024_salary_guide.pdf")
    print(data)
    output_file = "data/pickle/salary_guide_2024.pkl"
    pd.to_pickle(data, output_file)
    df = pd.DataFrame(data)
    print(df.head())