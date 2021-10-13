from datetime import datetime
from time import time
from pymongo import MongoClient
from minio import Minio, ResponseError
from minio.error import InvalidBucketError, InvalidBucketName, ResponseError, InvalidAccessKeyId, InvalidArgument, InvalidArgumentError, SignatureDoesNotMatch, AccessDenied, NoSuchKey
from subprocess import check_output, run
from minio_config import MINIO_CONFIG
import os 
import datetime
import json

class User:
    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password
    
    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def set_user(self):
        try:
            self.user = Minio(MINIO_CONFIG['MINIO_ENDPOINT'], 
                                    access_key=self.username, 
                                    secret_key=self.password, 
                                    secure=MINIO_CONFIG['MINIO_SECURE'])
            self.user.list_buckets()
            return {"msg":"User is now logged in", "status": "OK"}
        except SignatureDoesNotMatch as err: 
            return {"msg": err.message, "status":"F"}
        except ResponseError as err: 
            return {'msg': err.message, 'status': "F"}
        except InvalidAccessKeyId as err: 
            return {"msg": err.message, "status":"F"}
        except InvalidArgument as err: 
            return {"msg": err.message, "status":"F"}
        except InvalidArgumentError as err: 
            return {"msg": err.message, "status":"F"}

    def upload_file(self, file_as_stream, file_in_bytes, file_name):
        res = self.user.put_object(bucket_name=self.get_username(), 
                             object_name=file_name, 
                             data=file_as_stream, 
                             length=len(file_in_bytes)
                             )
        return res
    
    def download_file(self, file_name):
        try: 
            hr_file = self.user.get_object(bucket_name=self.get_username(), 
                                object_name=file_name)
            return hr_file.read()
        except ResponseError as err: 
            return {'error': err.message}
        except NoSuchKey as err: 
            return {'error': err.message}
        except AccessDenied as err: 
            return {'error': err.message}
        except InvalidBucketError as err: 
            return {'error': err.message}
        except InvalidBucketName as err: 
            return {'error': err.message}
