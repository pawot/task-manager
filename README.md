# Task manager  
## Setup  

Install and run Docker desktop
https://docs.docker.com/get-docker/  

Clone repository and navigate to it  
`$ git clone https://github.com/pawot/task-manager.git`  
`$ cd task-manager`  

Build Docker image  
`$ docker build -t task_manager .`  

Run the app  
`$ docker run -dp 8000:8000 task_manager`  

In browser navigate to http://localhost:8000/







