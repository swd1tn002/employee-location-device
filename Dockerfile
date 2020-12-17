FROM python:3-alpine

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY send-event.py .

CMD ["watch", "-n", "60", "python", "send-event.py"]