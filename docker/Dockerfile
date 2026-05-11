FROM python:3.11-slim

WORKDIR /app

COPY docker/app/backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY docker/app/backend/ .

EXPOSE 5000

CMD ["python", "app.py"]
