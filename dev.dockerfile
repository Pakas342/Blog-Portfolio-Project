# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container.
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
# We do it first because docker CACHE steps that don't change, and if we change the code and that stepo first,
# then everytime we're going to install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Dev version of the server
## Make port 5000 available to the world outside this container
#EXPOSE 5000
#
## Set environment variables
#ENV FLASK_APP=run.py
#ENV FLASK_RUN_HOST=0.0.0.0
#ENV ENV='DEV'
#
## Run the application
#CMD ["flask", "run"]



# Prod version of the server
# Make port available to the world outside this container
EXPOSE 8000

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=run.py
ENV PORT=8000
ENV ENV='PROD'

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "run:app"]