import json
import cv2
from pathlib import Path
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

for path in Path(BASE_FOLDER).rglob("*.jpg"):
    image = cv2.imread(f"{path}")[:,:,0]
    image = invert(image)
    out_data.append(image)
    
for out_image in out_data:
    in_image = cv2.resize(out_image, (OUT_SIZE, OUT_SIZE))
    in_image = cv2.threshold(in_image, 127, 255, cv2.THRESH_BINARY)
    in_data.append(in_image)
    print(in_image)

data = (in_data, out_data)

with open("data.json", "w") as outfile:
    json.dump(data, outfile)
