FROM python:3.8

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    apt-transport-https 

# Download and install Microsoft GPG key
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list | tee /etc/apt/sources.list.d/mssql-release.list

# Update the package list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
RUN /bin/bash -c "source ~/.bashrc"
RUN apt-get install -y unixodbc unixodbc-dev

# Set the working directory to /app
WORKDIR /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r /app/fdmgmt/requirements.txt
RUN pip install -e /app/fdmgmt/

# Make port 5000 available to the world outside this container
EXPOSE 23031

WORKDIR /app/fdmgmt/fdmgmt
CMD ["gunicorn", "api:app", "--bind", "0.0.0.0:23031"]
