FROM python:3.8

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN python -m pip install --upgrade pip && \
    python -m pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

EXPOSE 5000

CMD  uvicorn main:app --host 0.0.0.0 --port 5000 --reload
