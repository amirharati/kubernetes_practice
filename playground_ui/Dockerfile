FROM python:3.6
RUN mkdir -p /app/tmp
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["playground.py"]
