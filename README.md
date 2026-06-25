# LeetCode Tracker

A RESTful API built with FastAPI for tracking LeetCode practice, review progress, and spaced repetition schedules.

---

## Features

- RESTful API built with FastAPI
- Add, update, and delete LeetCode problems
- Search problems by title
- Filter problems by difficulty
- Filter problems by topic
- Mark problems as solved
- Track review history
- Detect overdue reviews using a spaced repetition schedule
- View practice statistics
- Prevent duplicate problem entries
- Interactive Swagger API documentation
- Dockerized deployment with Docker Compose

---

## Tech Stack

- Python 3
- FastAPI
- SQLite
- Pydantic
- Docker
- Docker Compose

---

## Project Structure

```text
leetcode-tracker/
├── api.py                 # REST API endpoints
├── services.py            # Business logic
├── database.py            # Database initialization
├── leetcode_sync.py       # LeetCode synchronization utility
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
├── .gitignore
└── README.md
```

> **Note:** `problems.db` is generated automatically at runtime and is not tracked in the repository.

---

## Installation

Clone the repository

```bash
git clone https://github.com/Joeytnc/leetcode-tracker.git
cd leetcode-tracker
```

Install dependencies

```bash
pip install -r requirements.txt
```

Initialize the database

```bash
python database.py
```

Run the application

```bash
uvicorn api:app --reload
```

The API will be available at:

```text
http://localhost:8000
```

Swagger UI:

```text
http://localhost:8000/docs
```

---

## Run with Docker

Build and start the application

```bash
docker compose up --build
```

Stop the application

```bash
docker compose down
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | API status |
| POST | /problems | Add a new problem |
| GET | /problems | Retrieve all problems |
| GET | /problems/{id} | Retrieve a problem by ID |
| PUT | /problems/{id} | Update a problem |
| DELETE | /problems/{id} | Delete a problem |
| GET | /problems/search | Search problems by title |
| GET | /problems/filter | Filter problems by difficulty |
| GET | /problems/topic | Filter problems by topic |
| POST | /problems/{id}/solve | Mark a problem as solved |
| POST | /problems/{id}/review | Record a review |
| GET | /reviews | Retrieve review history |
| GET | /reviews/overdue | Retrieve overdue reviews |
| GET | /reviews/today | Retrieve today's review list |
| GET | /stats | Retrieve practice statistics |

---

## Future Improvements

- JWT authentication
- PostgreSQL support
- Pagination
- Sorting
- Unit testing
- CI/CD pipeline
- Cloud deployment

---

## Learning Outcomes

This project demonstrates:

- RESTful API development
- CRUD operations
- FastAPI application design
- SQLite database management
- Request validation with Pydantic
- Spaced repetition scheduling
- Docker containerization
- Docker Compose deployment
- Backend project organization