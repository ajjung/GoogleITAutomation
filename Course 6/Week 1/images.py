#! /usr/bin/env python3

from PIL import Image
import os

source_dir="/Users/anthonyjung/Desktop/images/"
dest_dir="/Users/anthonyjung/Desktop/opt/icons/"
os.chdir(dest_dir)

for file in os.listdir(source_dir):
    if not file.startswith("."):
        with Image.open(os.path.join(source_dir,file)) as im:
            im.rotate(270).resize((128,128)).convert("RGB").save(file,"JPEG")
