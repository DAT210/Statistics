FROM python:3.7-slim

LABEL Author="Anders L"

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

ENV NAME Delivery

CMD [ "python", "testapp.py" ]
