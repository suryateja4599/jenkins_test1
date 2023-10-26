# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Install necessary packages and dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python libraries (PyMySQL and cryptography)
RUN pip install pymysql cryptography

# Copy the Python script into the container
COPY script.py /app/

# Specify the network to connect to
--network=mynetwork

# Run the Python script when the container launches
CMD ["python", "script.py"]

