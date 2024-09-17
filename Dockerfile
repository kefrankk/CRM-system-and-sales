# Use an official Python base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the dependency file (if you have one) to the container
COPY requirements.txt /app/

# Install project dependencies
RUN pip install -r requirements.txt

# Copy the contents of the current directory to the container
COPY . /app/

# Set the default command to run
CMD ["streamlit", "run", "app.py"]


