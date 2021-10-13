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

@app.route('upload/ehr', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        try:
            if 'file' in request.form:
                file = request.form['file']
                file_name = "file.txt"
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