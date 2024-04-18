FROM python:3.11
WORKDIR /opt

COPY . /opt
RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8086", "--reload"]