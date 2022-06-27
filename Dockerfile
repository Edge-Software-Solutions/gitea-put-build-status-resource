FROM python:3.6 as nodebuild

# install requirements
#ADD requirements*.txt setup.cfg ./
ADD requirements*.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# install asserts
#ADD assets/ /opt/resource/
#ADD test/ /opt/resource-tests/

#RUN /opt/resource-tests/test.sh



FROM python:3.6 as testbuild

# install requirements
COPY requirements*.txt ./
RUN pip install --no-cache-dir -r requirements_dev.txt
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    jq \
    && rm -rf /var/lib/apt/lists/*

# install asserts
WORKDIR /resource
COPY . .

RUN bash test/test.sh