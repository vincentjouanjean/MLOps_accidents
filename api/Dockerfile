FROM python:3.13-slim-bookworm

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/src

ENV PYTHONPATH=/code/src

CMD ["/bin/sh", "-c", "fastapi run /code/src/main.py --port 80"]
