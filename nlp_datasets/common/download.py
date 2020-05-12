import os
import requests
from tqdm import tqdm
from urllib.parse import urlparse

from nlp_datasets.urls.urls import dataset_urls


def download_file(dataset_name, temp_folder="."):
    path = dataset_urls[dataset_name]
    temp_path = os.path.join(temp_folder, filename_from_url(path))
    if os.path.exists(temp_path):
        return temp_path
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)
    with open(temp_path, "wb") as f:
        response = requests.get(path, stream=True)
        total_length = response.headers.get("content-length")

        if total_length is None:  # no content length header
            f.write(response.content)
        else:
            bar = tqdm(response.iter_content(chunk_size=4096), total=int(total_length))
            for data in bar:
                bar.update(len(data))
                f.write(data)
    return temp_path


def filename_from_url(url):
    a = urlparse(url)
    return os.path.basename(a.path)
