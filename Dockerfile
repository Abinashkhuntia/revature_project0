FROM python:3.11.9-slim-bookworm

WORKDIR /code

COPY . /code

# COPY ./requirements.txt /code/requirements.txt

RUN pip install -r /code/requirments.txt


# ENV DB_ENDPOINT="path"
# ENV DB_USERNAME="root"
# ENV DB_PASSWORD="toor"

EXPOSE 80


CMD  ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]