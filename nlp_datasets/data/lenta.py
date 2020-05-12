import os

import pandas as pd
from nlp_datasets.common.download import download_file


def load_lenta(temp_folder="."):
    path = download_file("lenta", temp_folder)
    df = pd.read_csv(path)
    result_path = os.path.join(temp_folder, "lenta.csv")
    df[["text", "topic", "tags"]].to_csv(result_path, index=False)
    return result_path
