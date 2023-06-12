# ThousandEyesChallenge Documentation

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

# References
  https://docs.docker.com/engine/
  https://developer.thousandeyes.com/v6/ 
