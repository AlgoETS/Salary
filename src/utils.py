
import pickle
import pandas as pd

def read_pickle(path):
    with open(path, "rb") as f:
        data = pickle.load(f)
    return data


def save_pickle(data, path):
    with open(path, "wb") as f:
        pickle.dump(data, f)


def load_data(path):
    data = read_pickle(path)


def load_dataframe(data):
    df = pd.DataFrame(data)


def save_dataframe(df, path):
    df.to_pickle(path)