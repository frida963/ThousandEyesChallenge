# ThousandEyesChallenge Documentation

To run the docker image, extract the archive (ThousandEyesAPI.zip) and proceed to build and run the Docker image using the provided Dockerfile.

Next are the steps followed to create the code and the docker image

# API code
Initialize a new virtual environment 

	python -m venv env 
	
	source env/bin/activate 
	  
Install necessary packages 

	pip install fastapi requests uvicorn 
	  
Save requirements 

	pip freeze > requirements.txt 
    
Test locally with 

	python -m uvicorn main:app --reload 
	  
http://localhost:8000/tests 
    



# Docker image
Create a Dockerfile

	Dockerfile
      # Use an official Python runtime as the base image
      FROM python:3.9-slim
      # Set the working directory in the container
      WORKDIR /app
      # Copy the requirements file to the container
      COPY requirements.txt .
      # Install the Python dependencies
      RUN pip install --no-cache-dir -r requirements.txt
      # Copy the rest of the application code to the container
      COPY . .
      # Expose the port used by FastAPI
      EXPOSE 8000
      # Start the FastAPI server
      CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
      
Build image

	sudo docker build -t myapi .
    
Run container

	sudo docker run -p 8000:8000 myapi
    
To view a list of all configured tests in my Thousand Eyes Account 

	http://localhost:8000/tests 
	
# Vulnerability Scan
Run a vulnerability scan on the container image

	(trivy installation required: https://github.com/aquasecurity/trivy#installation)
	
	trivy image myapi:latest

# Some results
myapi:latest (debian 11.7)

Total: 85 (UNKNOWN: 0, LOW: 65, MEDIUM: 2, HIGH: 17, CRITICAL: 1)

Library  

	Vulnerability 
	
	Severity 
	
	Installed Version
	
	Title     
apt 

	CVE-2011-3374

	LOW

	2.2.4

	It was found that apt-key in apt, all versions, do not correctly...  https://avd.aquasec.com/nvd/cve-2011-3374 

bash 

	CVE-2022-3715

	HIGH

	5.1-2+deb11u1
	
	a heap-buffer-overflow in valid_parameter_transform
	https://avd.aquasec.com/nvd/cve-2022-3715 


libdb5.3

	CVE-2019-8457

	CRITICAL

	5.3.28+dfsg1-0.8

	sqlite: heap out-of-bound read in function rtreenode()
	https://avd.aquasec.com/nvd/cve-2019-8457  


Based on the severity of the vulnerabilities found, appropriate actions should be taken.


# References
  https://docs.docker.com/engine/
  https://developer.thousandeyes.com/v6/ 
  https://github.com/aquasecurity/trivy#installation 
