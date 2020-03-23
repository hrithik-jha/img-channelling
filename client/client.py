import requests
import os
import cv2


target_path = "channels.tar.gz"

def sendImage(i):
    image_filename = os.path.basename(i)
    multipart_form_data = {
        'image': (image_filename, open(i, 'rb')),
    }
    response = requests.post('http://localhost:5000/upload', files=multipart_form_data)
    print(response)

    if response.status_code == 200:
        with open(target_path, 'wb') as f:
            f.write(response.raw.read())



file = "./file.png"
sendImage("./file.png")