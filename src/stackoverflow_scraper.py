# -*- coding: utf-8 -*-
import httpx
from bs4 import BeautifulSoup
from utils import save_pickle, load_dataframe

# make the request to the webpage
url = "https://survey.stackoverflow.co/2022/#salary-comp-total"
response = httpx.get(url)

# parse the HTML using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# find the salary table
salary_table = soup.find("table", {"id": "comp-totaldv46m"})

# create a dictionary to hold the salary data
salary_data = {}

# loop through the rows in the salary table
for row in salary_table.find_all("tr"):
    # get the cells in the row
    cells = row.find_all("td")

    # extract the data from the cells
    job_title = cells[0].get_text().strip()
    salary = cells[1].find("span", {"class": "js-bar-unit--label"}).get_text().strip()
    frequency = (
        cells[1].find("span", {"class": "js-bar-unit--frequency"}).get_text().strip()
    )

    # add the data to the dictionary
    salary_data[job_title] = {"salary": salary, "frequency": frequency}

# print the salary data
load_dataframe(salary_data)
save_pickle(salary_data, "data/pickle/stackoverflow_salary_data.pkl")
