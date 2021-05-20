FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /telstracodetest
WORKDIR /telstracodetest
COPY requirements.txt /telstracodetest/
RUN pip install -r requirements.txt
COPY . /telstracodetest/