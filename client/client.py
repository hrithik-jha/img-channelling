import requests
import os
import cv2


target_path = "channelsC.tar.gz"

def sendImage(i):
    image_filename = os.path.basename(i)
    multipart_form_data = {
        'image': (image_filename, open(i, 'rb')),
    }
    response = requests.post('http://localhost:5000/upload', files=multipart_form_data)
    print(response)

    



file = "./file.jpg"
sendImage("./file.jpg")