#! /usr/bin/env python3

import requests
import os

url = "http://localhost/upload/"
source_dir = "~/supplier-data/images"

for file in os.listdir(source_dir):
    if file.endswith(".jpeg"):
        with open(os.path.join(source_dir,file), 'rb') as opened:
            r = requests.post(url, files={'file':opened})
