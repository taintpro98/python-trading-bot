# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy project files
COPY ./bot /app/bot
COPY ./requirements.txt /app/requirements.txt
COPY .env /app/.env

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the app
CMD ["python", "-u", "/app/bot/main.py"]
