#! /usr/bin/env python3

import os
import requests
import re

source_dir = "supplier-data/descriptions/"
fruit_image = {
"Apple":"001.jpeg",
"Avocado":"002.jpeg",
"Blackberry":"003.jpeg",
"Grape":"004.jpeg",
"Kiwifruit":"005.jpeg",
"Lemon":"006.jpeg",
"Mango":"007.jpeg",
"Plum":"008.jpeg",
"Strawberry":"009.jpeg",
"Watermelon":"010.jpeg"
}
feedback = {}

for file in os.listdir(source_dir):
    if not file.startswith("."):
        with open(os.path.join(source_dir,file), "r") as text_file:
            feedback["name"] = text_file.readline().strip()
            weight = text_file.readline().strip()
            weight_re = re.search(r"(\d+)", weight)
            feedback["weight"] = weight_re[1]
            feedback["description"] = text_file.readline().strip()
            feedback["image_name"] = fruit_image[feedback["name"]]
    response = request.post("http://[linux-instance-external-IP]/fruits", data=feedback)
    if not response.ok:
        raise Exception("GET failed with status code {}".format(response.status_code))
