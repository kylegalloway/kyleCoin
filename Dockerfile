FROM python:3.7-alpine
LABEL maintainer="Kyle Galloway <kyle.galloway@cfdrc.com>"

# Install python packages
# COPY requirements.txt /
# RUN pip install -r requirements.txt

# Create source directory
ENV SRC_DIR /src
RUN mkdir ${SRC_DIR}
WORKDIR ${SRC_DIR}
VOLUME ${SRC_DIR}

CMD ["python", "main.py"]
