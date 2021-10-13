from flask import Flask, g, request, url_for, redirect, jsonify, render_template, make_response, Response
import os

from minio.error import MetadataTooLarge 
from user import User
from functools import wraps 
import jwt
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.exceptions import BadRequestKeyError
import datetime
import json 
import io
import re

app = Flask(__name__)

user = User()

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        try:
            if 'file' in request.form:
                file = request.files.getlist("file[]")
                file_name = "file"
                file_bytes = file.encode('utf-8')
                file_stream = io.BytesIO(file_bytes)

                res = user.upload_file(file_as_stream=file_stream,
                                            file_in_bytes=file_bytes,
                                            file_name=file_name)
                return res, 200
            return "file not found", 400
        except: 
            return "something went wrong", 400
    
    return '''
    <!doctype html>
    <title>stream_upload</title>
    <h1>stream_upload</h1>
    <form method=post enctype=multipart/form-data>
    <input type="text" name="hr_file" id="hr_file">
    <input type=submit value=Text>
    </form>
    '''

@app.route('/download', methods=['GET'])
def download_file():
    file_name = request.headers.get('file_name')
    file = user.download_file(file_name)
    if isinstance(file, dict): 
        return {'msg': file['error']}, 400
    return Response (
        file, 
        headers={"Content-Disposition": "attachment;filename=hr_file.txt"} 
    ), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')