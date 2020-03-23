from flask import Flask, request, redirect, url_for, flash, jsonify
import json
import os
from os import walk 
import sys

def imgName():
    files = os.listdir('./img/')
    return str(len(files) + 1)


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/img'

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
