#! /usr/bin/env python3

import os
import requests

source_dir = "/data/feedback"
feedback = {}

for file in os.listdir(source_dir):
    if not file.startswith("."):
        with open(os.path.join(source_dir,file), "r") as text_file:
            feedback["title"] = text_file.readline().strip()
            feedback["name"] = text_file.readline().strip()
            feedback["date"] = text_file.readline().strip()
            feedback["feedback"] = text_file.readline().strip()
    response = request.post("http://<corpweb-external-IP>/feedback", data=feedback)
    if not response.ok:
        raise Exception("GET failed with status code {}".format(response.status_code))
