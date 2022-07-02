FROM python:3.6 as test_build

# install requirements
COPY requirements*.txt ./
RUN pip install --no-cache-dir -r requirements_dev.txt
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    jq \
    && rm -rf /var/lib/apt/lists/* \

WORKDIR /opt/resource-test
COPY . .

COPY scripts /opt/resource

# install asserts

RUN bash test/test.sh

FROM python:3.6 as prod_build

COPY requirements*.txt ./
RUN pip install --no-cache-dir -r requirements.txt
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    jq \
    && rm -rf /var/lib/apt/lists/*

# install scripts
COPY scripts /opt/resource

