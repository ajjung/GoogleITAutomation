#! /usr/bin/env python3

from PIL import Image
import os

source_dir = "~/supplier-data/images"
#dest_dir="/Users/anthonyjung/Desktop/opt/icons/"
os.chdir(source_dir)

for file in os.listdir(source_dir):
    if file.endswith(".tiff"):
        with Image.open(os.path.join(source_dir,file)) as im:
            im.convert("RGB").resize((600,400)).save(file[:len(file)-4]+"jpeg","JPEG")
