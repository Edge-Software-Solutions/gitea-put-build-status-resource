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
# install asserts
WORKDIR /resource
COPY . .

RUN bash test/test.sh