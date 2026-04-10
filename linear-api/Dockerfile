FROM python:3.9-slim

WORKDIR /app

# Install flask without cache to ensure a clean build
RUN pip install --no-cache-dir flask

COPY app.py .

# Explicitly expose the required port [cite: 56]
EXPOSE 5000

CMD ["python", "app.py"]
