import json
import cv2
from pathlib import Path
import numpy as np
from settings import *


BASE_FOLDER = "C:\\proj\ml_data\\assorted_caracters\\"

def invert(image):
    size = len(image)
    for i in range(size):
        for j in range(size):
            image[i, j] = 255 - image[i, j]
    return image

out_data = []
in_data = []

print("reading images...")
for i, path in enumerate(Path(BASE_FOLDER).rglob("*.jpg")):
    if i >= MAX_TRAINING_FILES:
        break
    image = cv2.imread(f"{path}")[:,:,0]
    image = invert(image)
    out_data.append(image)
print(f"read {len(out_data)} files")

print("downscaling images...")
for out_image in out_data:
    in_image = cv2.resize(out_image, (IN_SIZE, IN_SIZE))
    in_image = cv2.threshold(in_image, 127, 255, cv2.THRESH_BINARY)
    in_data.append(in_image)

# convert to native lists
for i, element in enumerate(in_data):
    in_data[i] = element[1].tolist()
for i, element in enumerate(out_data):
    out_data[i] = element[1].tolist()

print("writing to file...")
data = (in_data, out_data)
with open("data.json", "w") as outfile:
    json.dump(data, outfile)
print("done")