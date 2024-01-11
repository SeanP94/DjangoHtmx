FROM python:3.11.4-alpine
WORKDIR /usr/src/app
# stops python from writing .pyc file
ENV PYTHONDONTWRITEBYTECODE 1
# Ensures python is sent to terminal, not buffer
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY ./entrypoint.sh usr/src/app/entrypoint.sh

COPY . /usr/src/app/

ENTRYPOINT ["./entrypoint.sh"]