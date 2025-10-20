# Backend Labs

### Course: Server Software Technologies

---

## Technologies Used
- Programming Language: Python 3.11+

- Web Framework: Flask

- Containerization: Docker

- Orchestration (Local): Docker Compose

- Version Control System: Git / GitHub

- Deployment: Render.com

---

## Local Project Launch (without Docker)

It is recommended to use a Python virtual environment for local execution.

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd <PROJECT_FOLDER_NAME>
```
### 2. Create and activate the virtual environment

```bash
python -m venv env
env\Scripts\activate  
```

### 3. Install dependencies

```bash
pip install flask
pip freeze > requirements.txt
```

### 4. Running the application

```bash
flask run --host 0.0.0.0 --port 8000
```

---

## Running with Docker

This method is recommended as it provides an isolated and reproducible environment.

### Requirements:

- Docker [installed](https://www.docker.com/).

### 1. Build the Docker Image

```bash
docker build . -t flask:lates
```

### 2. Run the Docker container

```bash
docker run -it --rm -p 8000:8000 -e PORT=8000 flask:latest

```
 ---

## Running with Docker Compose

```bash
docker-compose build
docker-compose up
```

---

## Deployment on Render.com

The [Render.com](https://render.com) platform is used for application deployment.

You can access this project **[here](https://backend-labs-ksx0.onrender.com/healthcheck)**.