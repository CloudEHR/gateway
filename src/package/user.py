from datetime import datetime
from time import time
# from pymongo import MongoClient
from minio import Minio
# from minio.error import InvalidBucketError, InvalidBucketName, ResponseError, InvalidAccessKeyId, InvalidArgument, InvalidArgumentError, SignatureDoesNotMatch, AccessDenied, NoSuchKey
from subprocess import check_output, run
from minio_config import MINIO_CONFIG
import os 
import datetime
import json

class User:
    def set_username(self):
        self.username = "minioadmin"

    def set_password(self):
        self.password = "minioadmin"
    
    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def set_user(self):
        # try:
        self.user = Minio(MINIO_CONFIG['MINIO_ENDPOINT'], 
                                access_key=MINIO_CONFIG['MINIO_ACCESS_KEY'], 
                                secret_key=MINIO_CONFIG['MINIO_SECRET_KEY'], 
                                secure=MINIO_CONFIG['MINIO_SECURE'])
        return {"msg":"User is now logged in", "status": "OK"}
        # except SignatureDoesNotMatch as err: 
        #     return {"msg": err.message, "status":"F"}
        # except ResponseError as err: 
        #     return {'msg': err.message, 'status': "F"}
        # except InvalidAccessKeyId as err: 
        #     return {"msg": err.message, "status":"F"}
        # except InvalidArgument as err: 
        #     return {"msg": err.message, "status":"F"}
        # except InvalidArgumentError as err: 
        #     return {"msg": err.message, "status":"F"}

    def upload_file(self, file_content, file_name):
        res = self.user.put_object(bucket_name='cloudehr', 
                            object_name=file_name, 
                            data=file_content
                            )
        print(str(res))
        return res
    
    def download_file(self, file_name):
        # try: 
        hr_file = self.user.get_object(bucket_name="cloudehr", 
                            object_name=file_name)
        return hr_file.read()
        # except ResponseError as err: 
        #     return {'error': err.message}
        # except NoSuchKey as err: 
        #     return {'error': err.message}
        # except AccessDenied as err: 
        #     return {'error': err.message}
        # except InvalidBucketError as err: 
        #     return {'error': err.message}
        # except InvalidBucketName as err: 
        #     return {'error': err.message}
