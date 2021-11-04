FROM ubuntu:18.04
RUN apt-get update 
RUN apt-get install -y python3 python3-pip
RUN mkdir /gateway
RUN mkdir -p /gateway/src/package
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
ADD /src /gateway/src
RUN ls /gateway
# ADD mc /gateway/mc
# ADD /src/package/__init__.py /gateway/src/__init__.py
# COPY /src/package/api.py /gateway/src/api.py
# COPY /src/package/minio_config.py /gateway/src/minio_config.py
# COPY /src/package/user.py /gateway/src/user.py

# RUN cd gateway; ./mc config host add cloudehr http://213.249.46.253:9000 minioadmin minioadmin
EXPOSE 5000
# WORKDIR /gateway
# ENTRYPOINT [ "ls" ]
ENTRYPOINT ["python3", "-u", "/gateway/src/package/api.py"]