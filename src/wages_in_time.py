import pandas as pd
import polars as pl
from utils import *
import os

WAGE_2012 = "data/csv/wage_2012.csv"
WAGE_2013 = "data/csv/wage_2013.csv"
WAGE_2014 = "data/csv/wage_2014.csv"
WAGE_2015 = "data/csv/wage_2015.csv"
WAGE_2016 = "data/csv/wage_2016.csv"
WAGE_2017 = "data/csv/wage_2017.csv"  # formatting error
WAGE_2018 = "data/csv/wage_2018.csv"  # formatting error
WAGE_2019 = "data/csv/wage_2019.csv"
WAGE_2020 = "data/csv/wage_2020.csv"
WAGE_2021 = "data/csv/wage_2021.csv"
WAGE_2022 = "data/csv/wage_2022.csv"

WAGES = [
    WAGE_2012,
    WAGE_2013,
    WAGE_2014,
    WAGE_2015,
    WAGE_2016,
    WAGE_2019,
    WAGE_2020,
    WAGE_2021,
    WAGE_2022,
]

WAGES_ALL = [
    WAGE_2012,
    WAGE_2013,
    WAGE_2014,
    WAGE_2015,
    WAGE_2016,
    WAGE_2017,
    WAGE_2018,
    WAGE_2019,
    WAGE_2020,
    WAGE_2021,
    WAGE_2022,
]


def load_data(filename):
    df = pl.DataFrame()
    try:
        df = pl.read_csv(
            filename,
            with_ignore_parser_errors=True,
            null_values=[""],
            low_memory=False,
            dtype={
                "Low_Wage_Salaire_Minium": pl.Float64,
                "Median_Wage_Salaire_Median": pl.Float64,
                "High_Wage_Salaire_Maximal": pl.Float64,
                "Annual_Wage_Flag_Salaire_Annuel": pl.Int64,
                "Annual_Wage_Flag_Salaire_annuel": pl.Int64,
            },
        )

    except Exception as e:
        print(f"Error reading {filename}: {e}")

    if "NOC Title" in df.columns:
        df = df.rename({"NOC Title": "NOC_Title"})

    if "Titre CNP" in df.columns:
        df = df.rename({"Titre CNP": "Titre_CNP"})

    if "NOC_Title_F" in df.columns:
        df = df.rename({"NOC_Title_F": "Titre_CNP"})
    # if exist rename the column
    if "NOC_Title_E" in df.columns:
        df = df.rename({"NOC_Title_E": "NOC_Title"})

    if "ER_Name_Nom_RE" in df.columns:
        df = df.rename({"ER_Name_Nom_RE": "Economic_Region"})

    if "Annual_Wage_Flag_Salaire_annuel" in df.columns:
        df = df.rename({"Annual_Wage_Flag_Salaire_annuel": "Annual_Wage_Flag_Salaire_Annuel"})

    # Keep only the columns we need
    df = df.select(
        [
            "NOC_Title",
            "Titre_CNP",
            "PROV",
            "Economic_Region",
            "Low_Wage_Salaire_Minium",
            "Median_Wage_Salaire_Median",
            "High_Wage_Salaire_Maximal",
            "Annual_Wage_Flag_Salaire_Annuel"
        ]
    )

    # Rename the columns
    df = df.rename(
        {
            "NOC_Title": "sector",
            "Titre_CNP": "job",
            "PROV": "province",
            "Economic_Region": "region",
            "Low_Wage_Salaire_Minium": "min_salary",
            "Median_Wage_Salaire_Median": "mid_salary",
            "High_Wage_Salaire_Maximal": "max_salary",
            "Annual_Wage_Flag_Salaire_Annuel": "annual_wage_flag"
        }
    )

    # add year to the dataframe with the year in the filename
    year = int(filename.split("_")[-1].split(".")[0])
    df = df.with_column(pl.lit(year).alias("year"))

    return df


def load_all_data():
    # if the pickle file exists, load it
    if os.path.exists("data/pickle/wages.pkl"):
        return read_pickle("data/pickle/wages.pkl")

    for wage in WAGES_ALL:
        print(f"Loading {wage}")
        df = load_data(wage)

    return pl.concat([load_data(wage) for wage in WAGES_ALL]).sort(
        "max_salary", reverse=True
    )


def higest_paying_job(df):
    # Sort the DataFrame by the maximum salary in descending order
    df_sorted = df.sort("max_salary", reverse=True)

    # Get the job that pays the most
    job_highest_paid = df_sorted["job"][0]
    maximum_salary = df_sorted["max_salary"][0]

    print(
        f"The job that pays the most is {job_highest_paid} with a maximum salary of {maximum_salary}"
    )

    return df_sorted.head()


def highest_paying_engineer(df):
    # Filter the DataFrame to only include jobs that contain the word "Engineer"
    df_filtered = df.filter(pl.col("sector").str.contains("Engineer"))

    # remove the missing max salary
    df_filtered = df_filtered.filter(pl.col("max_salary").is_not_null())

    # Sort the DataFrame by the maximum salary in descending order
    df_sorted = df_filtered.sort("max_salary", reverse=True)

    # Get the job that pays the most
    job_highest_paid = df_sorted["job"][0]
    maximum_salary = df_sorted["max_salary"][0]
    province = df_sorted["province"][0]
    year = df_sorted["year"][0]

    print(
        f"The job that pays the most is {job_highest_paid} with a maximum salary of {maximum_salary * 40 * 45} in the province of {province}"
    )

    return df_sorted.head()


def highest_paying_engineer_for_each_province(df):
    # Filter the DataFrame to only include jobs that contain the word "Engineer"
    df_filtered = df.filter(pl.col("sector").str.contains("Engineer"))

    # remove the missing max salary
    df_filtered = df_filtered.filter(pl.col("max_salary").is_not_null())

    # Sort the DataFrame by the maximum salary in descending order
    df_sorted = df_filtered.sort("max_salary", reverse=True)

    # Group the DataFrame by province and get the first row of each group
    df_grouped = df_sorted.groupby("province").first()

    df_sorted = df_grouped.sort("max_salary", reverse=True)

    for i in range(len(df_sorted)):
        max_salary = df_sorted["max_salary"][i] * 45 * 45
        print(
            f"The job that pays the most in {df_sorted['province'][i]} is {df_sorted['job'][i]} with a maximum salary of {max_salary}"
        )

def highest_for_each_year(df):
    # Group the DataFrame by year and get the first row of each group
    df_grouped = df.groupby("year").first()

    # Sort the DataFrame by the maximum salary in descending order
    df_sorted = df_grouped.sort("max_salary", reverse=True)


    for i in range(len(df_sorted)):
        print(
            f"The job that pays the most in {df_sorted['year'][i]} is {df_sorted['job'][i]} with a maximum salary of {df_sorted['max_salary'][i]} in the {df_sorted['province'][i]}"
        )



if __name__ == "__main__":
    df = load_all_data()
    save_pickle(df, "data/pickle/wages.pkl")
    higest_paying_job(df)
    highest_for_each_year(df)
    highest_paying_engineer(df)
    highest_paying_engineer_for_each_province(df)
