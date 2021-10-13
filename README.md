# gateway
The Gateway of the EHR Cloud


How to use Minio Client: 

Change permission to allow execution to the mc file: 

    chmod +rwx mc

#### 1. Connect to the minio server: 
Connect to the minio server docker container from the minio client docker container with administrative rights

	mc config host add $(MINIO_SERVER_FRIENDLY_NAME) http://127.0.0.1:9000 $(ACCESS_KEY) $(SECRET_KEY)