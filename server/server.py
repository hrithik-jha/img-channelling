from flask import Flask, request, redirect, url_for, flash, jsonify
import json
import os
from os import walk 
import sys
import cv2

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/img'

def imgName():
    files = os.listdir('./img/')
    return str(len(files) + 1)



def splitChannels(imgFile):
        b, g, r = cv2.split(imgFile)
        cv2.imwrite('./channels/blue.jpg', b)
        cv2.imwrite('./channels/green.jpg', g)
        cv2.imwrite('./channels/red.jpg', r)
        return createCompression()

@app.route('/')
def hello():
        return "Server is listening..."

@app.route('/upload', methods=['POST'])
def index():
        file1 = request.files['image']
        nom = "./img/" + str(imgName()) + ".png"
        file1.save(nom)
        #detectImage(nom)
        return "File Saved"
        

if __name__ == '__main__':
        app.run()
