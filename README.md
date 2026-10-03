# Server Monitor

## Problem
Manual server monitoring is slow and error-prone.

## Solution
A Dockerized Python script that reads CPU, Memory, and Disk usage in real-time and serves the result as an HTML dashboard via nginx.

## Architecture
- **monitor**: Python + psutil → writes index.html
- **web**: nginx → serves index.html on port 8080

## How to Run
```bash
docker-compose up -d
```
Open http://localhost:8080

## Technologies
- Python, psutil
- Docker, Docker Compose
- nginx
