FROM python:3.11.2-alpine

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["flask_app.py"]