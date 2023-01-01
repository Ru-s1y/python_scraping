FROM python:3.11

WORKDIR /var/app

# linux
RUN apt-get update
RUN apt-get install -y sudo less vim zip unzip python3-selenium
RUN apt-get install -y sudo less vim zip unzip

# Japanese
ENV LANGUAGE ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
RUN apt-get install -y --no-install-recommends locales && \
    locale-gen ja_JP.UTF-8 && \
    # 日本語フォントをインストール
    apt-get install -y --no-install-recommends fonts-ipafont

# chrome driver
ADD https://chromedriver.storage.googleapis.com/109.0.5414.25/chromedriver_linux64.zip /opt/chrome/
RUN cd /opt/chrome/ && \
    unzip chromedriver_linux64.zip && \
    rm -f chromedriver_linux64.zip
RUN mv /opt/chrome/chromedriver /usr/bin/chromedriver

# python
RUN pip install --upgrade pip
COPY requirements.txt /var/app
RUN pip install -r requirements.txt
