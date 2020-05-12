import os

import pandas as pd
from zipfile import ZipFile
from nlp_datasets.common.download import download_file


def load_reviews(temp_folder="."):
    path = download_file("reviews", temp_folder)
    with ZipFile(path) as zip_file:
        zip_file.extract("all.csv", temp_folder)
    df = pd.read_csv(os.path.join(temp_folder, "all.csv"))
    df = df[(df["language"] == "russian") & (~df["rating"].isnull())]
    df["rating"] = df["rating"].astype(int)
    df = df.fillna("")
    df["text"] = df["text"] + " " + df["plus"] + " " + df["minus"]
    df["text"] = df["text"].str.strip()
    df = df[["text", "rating", "category"]]
    result_path = os.path.join(temp_folder, "reviews.csv")
    df.to_csv(result_path, index=False)
    os.remove(path)
    os.remove(os.path.join(temp_folder, "all.csv"))
    return result_path
