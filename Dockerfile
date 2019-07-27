# Use an official Python runtime as a parent image
FROM ubuntu:18.04

RUN apt-get update && apt-get install -y vim

RUN apt-get install -y git

RUN apt-get install -y python3-pip

# Sqlite 3
RUN apt-get install sqlite3

# Set the working directory to /Project
WORKDIR /Project

# Copy the current directory contents into the container at /app
COPY requirements.txt /Project

# Install any needed packages specified in requirements.txt
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

# Set the working directory to /Project/MIT_Final_Project
WORKDIR /Project/MIT_Final_Project

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World
