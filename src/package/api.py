from flask import Flask, g, request, url_for, redirect, jsonify, render_template, make_response, Response
import os

# from minio.error import MetadataTooLarge 
from user import User
from functools import wraps 
# import jwt
# from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.exceptions import BadRequestKeyError
import datetime
import json 
import io
import re

app = Flask(__name__)

user = User()
user.set_user()
file_prefetched = user.download_file("test5.txt")


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        try:
            if 'file' not in request.files:
                return "file not chosen", 400
            else:
                file = request.files["file"]
                file_name = file.filename
                file_bytes = file.read()
                user.set_user()
                res = user.upload_file(file_content=file_bytes,
                                            # file_in_bytes=file_bytes,
                                            file_name=file_name)
                return res
        except: 
            return "something went wrong", 400
    
    return '''
    <!doctype html>
    <title>stream_upload</title>
    <h1>stream_upload</h1>
    <form method=post enctype=multipart/form-data>
    <input type="file" name="file" multiple="">
    <input type=submit value=Upload>
    </form>
    '''

@app.route('/download', methods=['GET'])
def download_file():
    file_name = request.headers.get('file_name')
    user.set_user()
    file = user.download_file(file_name)
    if isinstance(file, dict): 
        return {'msg': file['error']}, 400
    return Response (
        file, 
        headers={"Content-Disposition": "attachment;filename=hr_file.txt"} 
    ), 200

@app.route('/downloadPrefetch', methods=['GET'])
def download_file_prefetch():
    file_name = request.headers.get('file_name')
    return Response (
        file_prefetched, 
        headers={"Content-Disposition": "attachment;filename=hr_file.txt"} 
    ), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')