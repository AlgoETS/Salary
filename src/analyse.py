# -*- coding: utf-8 -*-

def highest_paying_job(df):
    # Split the salary ranges into minimum and maximum salaries
    df[["entry_min", "entry_max"]] = (
        df["entry"].str.split("-", expand=True).astype(float)
    )
    df[["mid_min", "mid_max"]] = df["mid"].str.split("-", expand=True).astype(float)
    df[["senior_min", "senior_max"]] = (
        df["senior"].str.split("-", expand=True).astype(float)
    )

    # Create a new column with the maximum salary for each job
    df["max_salary"] = df[["entry_max", "mid_max", "senior_max"]].max(axis=1)
    # calculate the mean for each level
    df["entry_mean"] = df[["entry_min", "entry_max"]].mean(axis=1)
    df["mid_mean"] = df[["mid_min", "mid_max"]].mean(axis=1)
    df["senior_mean"] = df[["senior_min", "senior_max"]].mean(axis=1)

    # Sort the DataFrame by the maximum salary in descending order
    df_sorted = df.sort_values("max_salary", ascending=False)

    # Get the job that pays the most
    job_highest_paid = df_sorted["job"].iloc[0]

    print(f"The job that pays the most is {job_highest_paid}")

    return df_sorted.head()


def highest_paying_engineer(df_sorted):
    top_engineers_jobs = df_sorted[
        df_sorted["job"].str.contains("engineer", case=False)
    ]
    print(f"The job that pays the most is {top_engineers_jobs}")
    return top_engineers_jobs.head(30)


def lowest_paying_job(df_sorted):
    worst_engineers_jobs = df_sorted.sort_values("max_salary", ascending=True)
    top30 = worst_engineers_jobs.head(30)
    print(f"The job that pays the least is {worst_engineers_jobs}")


def highest_paying_quebec(df_sorted):
    top_quebec_jobs = df_sorted[
        df_sorted["province"].str.contains("québec", case=False)
    ]
    print(f"The job that pays the most in Quebec is {top_quebec_jobs}")
    return top_quebec_jobs.head(30)


# make a function to compare a specific job in a specific province
def compare_job_province(df, job, province):
    df_filtered = df[(df["province"] == province) & (df["job"] == job)]
    df_grouped = df_filtered.groupby(["job", "region"])["mid_mean"].mean().reset_index()
    return df_grouped.sort_values("mid_mean", ascending=False)


def compare_job(df, job):
    df_filtered = df[df["job"] == job]
    df_grouped = df_filtered.groupby(["job", "region"])["mid_mean"].mean().reset_index()
    return df_grouped.sort_values("mid_mean", ascending=False)


def compare_province(df, province):
    df_filtered = df[df["province"] == province]
    df_grouped = df_filtered.groupby(["job", "region"])["mid_mean"].mean().reset_index()
    return df_grouped.sort_values("mid_mean", ascending=False)


def compare_job_region(df, job, region):
    df_filtered = df[(df["region"] == region) & (df["job"] == job)]
    df_grouped = df_filtered.groupby(["job", "region"])["mid_mean"].mean().reset_index()
    return df_grouped.sort_values("mid_mean", ascending=False)


# function to compare a specific job in a all provinces
def compare_job_all_provinces(df, job):
    df_filtered = df[(df["job"] == job)]
    df_grouped = (
        df_filtered.groupby(["job", "province"])["mid_mean"].mean().reset_index()
    )
    return df_grouped.sort_values("mid_mean", ascending=False)


# function to find the job with the largest difference, the user can choose between entry, mid or senior
def find_job_with_biggest_diff(df, level):
    # if level is not entry, mid or senior, return an error
    if level not in ["entry_mean", "mid_mean", "senior_mean"]:
        return "Error: level must be entry_mean, mid_mean or senior_mean"
    # Group by the 'job' column and find the difference between the maximum and minimum values of the 'mid' column for each group
    job_diffs = df.groupby("job")[[level]].apply(lambda x: (x.max() - x.min()).sum())

    # Find the job with the largest overall salary difference
    max_diff_job = job_diffs.idxmax()

    # Print the result
    print(f"The job with the largest overall salary difference is: {max_diff_job}")

    return max_diff_job


# Detailled breakdown of the salary by province
def salary_breakdown_by_province(df, job="cloud architect"):
    # Get the unique provinces
    provinces = df["province"].unique()

    # Loop over the provinces and compare the job in each province
    for province in provinces:
        # Filter the dataframe by province and job
        df_filtered = df[(df["province"] == province) & (df["job"] == job)]

        # Group the resulting dataframe by job and region, and calculate the mean mid salary
        df_grouped = (
            df_filtered.groupby(["job", "region"])["mid_mean"].mean().reset_index()
        )

        # Sort the grouped dataframe by the mid salary in descending order
        df_sorted = df_grouped.sort_values("mid_mean", ascending=False)

        # Print the sorted dataframe with the province name
        print(f"{province.capitalize()}:")
        print(df_sorted)
        print()
