# 🛰️ Django WebSocket Real-Time

This project is a real-time WebSocket communication in Django using Channels, Redis, and PostgreSQL. It includes:

- A live date/time broadcast to all connected clients.
- Fibonacci calculation sent privately to the requester.
- Connected users saved in the database.
- Dockerized environment for easy setup.

---

## 🚀 Features

- Real-time communication using Django Channels
- Redis for channel layer messaging
- PostgreSQL as the main database
- WebSocket client on frontend
- Docker development environment

---

## 📦 Requirements

- Docker
- Docker Compose

---

## 🔧 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Diogo-d-Souza/bsa-tech.git
cd bsa-tech
```

### 2. Change the name of the file `.env-setup` to `.env`

This file is related to the environment settings for the application and you can stay as it is to test it in localhost.

### 3. Build and run the containers

```bash
docker compose up --build -d
```

This will start:
- Django backend (on port `8000`)
- PostgreSQL (on port `5434`)
- Redis (on port `6379`)

### 4. Run database migrations

```bash
docker compose exec back python manage.py migrate
```

### 5. Access the application

Go to:
[http://localhost:8000/users/websocket/](http://localhost:8000/users/websocket/)

You will see a simple page with:
- Real-time clock
- Input to calculate Fibonacci numbers

---

## 🧪 Testing WebSocket

You can use **Postman** or **Insomnia** with the WebSocket feature.
WebSocket URL: `ws://localhost:8000/ws/`

Send a JSON message like:

```json
{ "n": 10 }
```

You will receive the Fibonacci result privately.

---

## 🧼 Stopping Everything

To stop the containers:

```bash
docker-compose down
```

---