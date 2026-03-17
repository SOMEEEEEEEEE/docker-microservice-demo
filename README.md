# Docker Flask API

A simple Flask API containerized with Docker and deployed on an Ubuntu EC2 instance.  
This project demonstrates basic DevOps practices including containerization, API deployment, and cloud testing.

> Note: This is a demo project for learning and practice purposes.

---

## Project Structure

 	docker-flask-api
 	│
	├── app.py
 	├── requirements.txt
 	├── Dockerfile
 	└── README.md

---

## Features

- Simple Flask API
- Docker containerization
- Runs on Ubuntu EC2
- Accessible via HTTP API
- Health check endpoint for monitoring service status (03/16)

---

## Tech Stack

- Python
- Flask
- Docker
- Ubuntu
- AWS EC2

---

## API Endpoint

GET /

Response:

Hello from Docker Flask API!

---

### GET /health

Response:

```json
{
  "status": "healthy"
}