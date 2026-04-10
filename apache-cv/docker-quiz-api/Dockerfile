# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install Flask
RUN pip install flask

# Copy the API script into the container
COPY app.py .

# Expose port 5000 [cite: 56]
EXPOSE 5000

# Command to run the API
CMD ["python", "app.py"]
