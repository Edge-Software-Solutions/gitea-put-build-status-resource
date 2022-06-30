<<<<<<< HEAD
FROM python:3.6 AS concourse_resource_build

=======
FROM python:3.6 as concourse_resource_test

# install requirements
COPY requirements*.txt ./
RUN pip install --no-cache-dir -r requirements_dev.txt
>>>>>>> master
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    jq \
    && rm -rf /var/lib/apt/lists/*
<<<<<<< HEAD

# install assets
ADD scripts/ /opt/resource/
RUN chmod +x /opt/resource/*
WORKDIR /opt/resource


FROM python:3.6 AS concourse_resource_test
=======

# install asserts
WORKDIR /opt/resource-test
COPY . .

RUN bash test/test.sh


FROM python:3.6 as concourse_resource_run
>>>>>>> master

# install requirements
COPY requirements*.txt ./
RUN pip install --no-cache-dir -r requirements_dev.txt
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    jq \
    && rm -rf /var/lib/apt/lists/*

<<<<<<< HEAD
# install asserts
WORKDIR /opt/resource-test
COPY . .

RUN bash test/test.sh


=======
# install assets
ADD scripts/ /opt/resource/
RUN chmod +x /opt/resource/*
WORKDIR /opt/resource
>>>>>>> master
