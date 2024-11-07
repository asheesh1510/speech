# Use an official Python base image
FROM python:3.11

# Install system dependencies for Rust (if needed)
RUN apt-get update && apt-get install -y \
    build-essential \
    rustc \
    cargo \
    && apt-get clean

# Set the working directory in the container
WORKDIR /app

# Copy your requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application into the container
COPY . .

# Set the environment variable for Flask or another web framework (if needed)
ENV FLASK_APP=app.py

# Expose the port your application will run on
EXPOSE 5000

# Command to run your app
CMD ["python", "app.py"]
