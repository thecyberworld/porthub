FROM python:3.8

ADD . .

CMD ["python3", "scanner.py"]
