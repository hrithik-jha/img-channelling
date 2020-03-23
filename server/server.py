from flask import Flask, request, redirect, url_for, flash, jsonify, send_file
import json
import os
from os import walk 
import sys
import cv2
import tarfile

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/img'

def imgName():
        files = os.listdir('./img/')
        return str(len(files) + 1)

def createCompression():
        source_dir = './channels'
        output_filename = 'channelsC.tar.gz'
        with tarfile.open(output_filename, "w:gz") as tar:
                tar.add(source_dir, arcname=os.path.basename(source_dir))
        print("tar file created\n")
        return "output_filename"

def splitChannels(imgFile):
        img = cv2.imread(imgFile)
        b, g, r = cv2.split(img)

        print(len(b.shape))

        cv2.imwrite('C:\\Users\\Hrithik Jha\\hd-imaging-sol\\server\\channels\\blue.jpg', b)
        cv2.imwrite('C:\\Users\Hrithik Jha\\hd-imaging-sol\\server\\channels\\green.jpg', g)
        cv2.imwrite('C:\\Users\Hrithik Jha\\hd-imaging-sol\\server\\channels\\red.jpg', r)
        print("colour channels split\n")
        return 

@app.route('/')
def hello():
        return "Server is listening..."

@app.route('/upload', methods=['POST'])
def index():
        file1 = request.files['image']
        nom = "./img/" + str(imgName()) + ".jpg"
        file1.save(nom)
        splitChannels(nom)
        print("returning tar file\n")
        return "Consequent request ready" #send_file(fileC, as_attachment=True)

@app.route('/images', methods=['GET'])
def imgReturn():
        col = request.args.get('col')
        print(request.args)
        if col == "red":
                return send_file('C:\\Users\\Hrithik Jha\\hd-imaging-sol\\server\\channels\\red.jpg', mimetype='image/jpg')
        elif col == "blue":
                return send_file('C:\\Users\\Hrithik Jha\\hd-imaging-sol\\server\\channels\\blue.jpg', mimetype='image/jpg')
        elif col == "green":
                return send_file('C:\\Users\\Hrithik Jha\\hd-imaging-sol\\server\\channels\\green.jpg', mimetype='image/jpg')
        else:
                return "No colour argument"

if __name__ == '__main__':
        app.run()
