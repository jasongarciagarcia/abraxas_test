FROM python:2.7
MAINTAINER Roberto Jason "jason@gnuin0.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
