FROM python:3.9-alpine

RUN apk add bash 
RUN mkdir -p /app
WORKDIR /app

COPY . . 

RUN  pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["bash"]
