# syntax=docker/dockerfile:1
FROM python:3.7
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
# dont know what this is for but fails on M1
# RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 80
#COPY ./app .
CMD ["python", "app/app.py"]
