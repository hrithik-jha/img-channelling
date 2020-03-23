import requests
import os
import cv2
import shutil
import numpy as np


def mergeChannels():
    print("Merging...")
    b = cv2.imread('blue.jpg', cv2.IMREAD_GRAYSCALE)
    r = cv2.imread('red.jpg', cv2.IMREAD_GRAYSCALE)
    g = cv2.imread('green.jpg', cv2.IMREAD_GRAYSCALE)

    image = cv2.merge((b, g, r))
    print(image.shape)
    cv2.imwrite('merged.jpg', image)
    
def sendImage(i):
    image_filename = os.path.basename(i)
    multipart_form_data = {
        'image': (image_filename, open(i, 'rb')),
    }
    response = requests.post('http://localhost:5000/upload', files=multipart_form_data)
    print(response)

    url = 'http://localhost:5000/images?col='
    queries = ['red', 'green', 'blue']
    if response.status_code == 200:
        for i in queries:
            response = requests.get(url + i, stream=True)
            with open(i+'.jpg', 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
    mergeChannels()



file = "./file.jpg"
sendImage("./file.jpg")