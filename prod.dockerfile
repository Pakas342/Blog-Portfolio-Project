# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
# We do it first because docker CACHE steps that don't change, and if we change the code and that stepo first,
# then everytime we're going to install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

## Make port available to the world outside this container (not necesary on gCP run as they open another port)
#EXPOSE 8000

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=run.py
#(not necesary on gCP run as tehy automaticlly do it)
#ENV PORT=8000
ENV ENV='PROD'

# Run the application
CMD gunicorn --bind 0.0.0.0:$PORT run:app