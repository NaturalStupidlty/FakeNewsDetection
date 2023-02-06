FROM python:3.8-alpine

# copy every content from the local file to the image
COPY . /app

# switch working directory
WORKDIR /app

RUN pip freeze > requirements.txt
# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD flask run --host 0.0.0.0