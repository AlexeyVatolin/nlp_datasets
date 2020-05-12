import os

import pandas as pd

from nlp_datasets.common.download import download_file


def load_banki_ru(temp_folder):
    path = download_file("banki_ru", temp_folder)
    df = pd.read_csv(path)
    result_path = os.path.join(temp_folder, "banki_ru.csv")
    df[["text", "rating", "target"]].to_csv(result_path, index=False)
    return result_path
