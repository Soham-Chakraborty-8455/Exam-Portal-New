FROM python:3.10.6

RUN pip install -r requirements.txt

CMD=["python","app.py"]