import requests
import os
import cv2
import shutil


def mergeChannels():
    print("Merging...")
    b = cv2.imread('blue.jpg')
    r = cv2.imread('red.jpg')
    g = cv2.imread('green.jpg')

    #image = cv2.merge((b, g, r))
    image = cv2.merge([b, g, r]);
    merged = cv2.cvtColor(image,cv2.CV_HSV2BGR);
    cv2.imwrite('merged.jpg', merged)
    
def sendImage(i):
    image_filename = os.path.basename(i)
    multipart_form_data = {
        'image': (image_filename, open(i, 'rb')),
    }
    response = requests.post('http://localhost:5000/upload', files=multipart_form_data)
    print(response)


    queries = ['red', 'green', 'blue']
    if response.status_code == 200:
        for i in queries:
            response = requests.get('http://localhost:5000/images?col=' + i, stream=True)
            with open(i+'.jpg', 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
    mergeChannels()



file = "./file.jpg"
sendImage("./file.jpg")