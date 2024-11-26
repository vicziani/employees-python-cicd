FROM python:3.13.0-slim-bullseye
RUN apt-get -y update; apt-get -y install curl
WORKDIR /app
COPY *.toml *.txt .
RUN pip install -c constraints.txt .
COPY src .
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:5000", "employees:app"]