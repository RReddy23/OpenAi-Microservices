# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy only the shared requirements file
COPY ../../requirements.txt /app/requirements.txt

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the service source code
COPY . /app

# Expose service port
EXPOSE 8000

# Command to run the service
CMD ["uvicorn", "api_gateway.main:app", "--host", "0.0.0.0", "--port", "8000"]
