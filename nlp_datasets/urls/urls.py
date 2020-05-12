import os
import json

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "urls.json")) as f:
    dataset_urls = json.load(f)
