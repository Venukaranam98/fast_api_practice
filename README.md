# FastAPI Backend Practice

A hands-on backend development repository focused on building scalable REST APIs using FastAPI, PostgreSQL, SQLAlchemy, Redis, JWT Authentication, and Alembic.

This repository contains practical implementations of core backend concepts including authentication, database migrations, caching, rate limiting, Pub/Sub messaging, and CRUD operations.

---

## Features

### Authentication & Authorization

* User Registration
* User Login
* JWT Token Authentication
* Password Hashing with Passlib
* Protected Routes

### Database Management

* PostgreSQL Integration
* SQLAlchemy ORM
* Alembic Database Migrations

### API Development

* RESTful API Design
* CRUD Operations
* Request Validation with Pydantic
* Dependency Injection

### Redis

* Redis Strings
* Hashes
* Lists
* TTL (Time To Live)
* Cache-Aside Pattern
* Redis Pub/Sub
* Persistence (RDB vs AOF)
* Eviction Policies (LRU)
* Login Rate Limiting
* API Response Caching

---

## Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy
* Alembic
* Redis
* JWT Authentication
* Passlib
* Pydantic
* Docker
* Uvicorn

---

## Project Structure

```text
FASTAPI/
├── alembic/
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
│
├── FastAPI/
│   ├── routers/
│   │   ├── auth.py
│   │   ├── posts.py
│   │   └── students.py
│   │
│   ├── redis_practice/
│   │   ├── 01_strings.py
│   │   ├── 02_ttl.py
│   │   ├── 03_hashes.py
│   │   ├── 04_lists.py
│   │   ├── 05_caching_demo.py
│   │   ├── publisher.py
│   │   ├── subscriber.py
│   │   └── redis_client.py
│   │
│   ├── .env
│   ├── crud.py
│   ├── database.py
│   ├── hashing.py
│   ├── jwt_handler.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
│
├── .gitignore
├── alembic.ini
├── requirements.txt
└── README.md
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/fast_api_practice.git

cd fast_api_practice
```

### 2. Create and Activate Virtual Environment

#### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file inside the `FastAPI/` directory:

```env
DATABASE_URL=your_postgresql_connection_string
SECRET_KEY=your_secret_key
```

### 5. Run Database Migrations

```bash
alembic upgrade head
```

### 6. Start Redis

```bash
docker run -d --name redis -p 6379:6379 redis
```

### 7. Run the Application

```bash
uvicorn FastAPI.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

to access the interactive Swagger UI.

---

## Redis Practice Modules

Navigate to:

```bash
cd FastAPI/redis_practice
```

Run examples:

```bash
python 01_strings.py
python 02_ttl.py
python 03_hashes.py
python 04_lists.py
python 05_caching_demo.py
```

Pub/Sub example:

Terminal 1:

```bash
python subscriber.py
```

Terminal 2:

```bash
python publisher.py
```

---
