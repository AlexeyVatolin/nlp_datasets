import os

import pandas as pd

from nlp_datasets.common.download import download_file


def load_agrr(temp_folder):
    dataset_path = []
    for name in ["agrr_train", "agrr_dev"]:
        path = download_file(name, temp_folder)
        df = pd.read_csv(path, sep="\t")
        df = df[~df["class"].isnull()]
        df["class"] = df["class"].astype(int)
        result_path = os.path.join(temp_folder, name + ".csv")
        df[["text", "class"]].to_csv(result_path, index=False)
        dataset_path.append(result_path)
        os.remove(path)
    return dataset_path
