from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import Enum
from services import (
    add_problem, get_all_problems, get_problem_by_id, update_problem_by_id, delete_problem_by_id,
    get_stats, review_problem_by_id, get_review_history, get_today_reviews, mark_problem_solved,
    get_problems_by_difficulty, get_problem_by_topic, search_problems, problem_exists
)
from database import initialize_database

initialize_database()

tags_metadata = [
    {
        "name": "System",
        "description": "Application status endpoints"

    },
    {
        "name": "Problems",
        "description": "Manage LeetCode problems."

    },
    {
        "name": "Reviews",
        "description": "Review history and spaced repetition."

    },
    {
        "name": "Statistics",
        "description": "Practice statistics."

    }
]

app = FastAPI(
    title="LeetCode Tracker API",
    description="RESTful API for managing LeetCode problems, tracking practice progress, and scheduling reviews using spaced repetition.",
    version="1.0.0"
)


class Difficulty(str, Enum):
    EASY = "Easy"
    MEDIUM = "Medium"
    HARD = "Hard"

class ProblemCreate(BaseModel):
    title: str
    difficulty: Difficulty
    topic: str


@app.get("/", tags=["System"])
def root():

    return {"message": "LeetCode Tracker API running"}

@app.post("/problems", tags=["Problems"])
def create_problems(problem: ProblemCreate):

    if problem_exists(problem.title):

        raise HTTPException(
            status_code=400,
            detail="Problem already exists"
        )

    add_problem(
        problem.title,
        problem.difficulty,
        problem.topic,
    )

    return {"message": "Problem added successfully"}

@app.get("/problems", tags=["Problems"])
def get_problems():

    return get_all_problems()

@app.get("/problems/search", tags=["Problems"])
def search(keyword: str):

    return search_problems(keyword)

@app.get("/problems/topic", tags=["Problems"])
def get_problems_topic(topic: str):

    return get_problem_by_topic(topic)

@app.get("/problems/filter", tags=["Problems"])
def filter_problems(difficulty: str):

    return get_problems_by_difficulty(difficulty)

@app.get("/problems/{problem_id}", tags=["Problems"])
def get_problem(problem_id:int):

    problem = get_problem_by_id(problem_id)

    if problem:
        return problem
    raise HTTPException(
        status_code=404,
        detail="Problem not found"
    )

@app.put("/problems/{problem_id}", tags=["Problems"])
def update_problem(problem_id:int, problem: ProblemCreate):

    updated_problem = update_problem_by_id(
        problem_id,
        problem.title,
        problem.difficulty,
        problem.topic,
    )

    if updated_problem:
        return {"message": "Problem updated successfully"}
    raise HTTPException(
        status_code=404,
        detail="Problem not found"
    )

@app.delete("/problems/{problem_id}", tags=["Problems"])
def delete_problem(problem_id:int):

    deleted_problem = delete_problem_by_id(problem_id)
    if deleted_problem:
        return {"message": "Problem deleted successfully"}
    raise HTTPException(
        status_code=404,
        detail="Problem not found"
    )

@app.post("/problems/{problem_id}/review", tags=["Problems"])
def review_problem(problem_id:int):

    reviewed = review_problem_by_id(problem_id)
    if reviewed:
        return {"message": "Problem reviewed successfully"}
    raise HTTPException(
        status_code=404,
        detail="Problem not found"
    )

@app.post("/problems/{problem_id}/solve", tags=["Problems"])
def solve_problem(problem_id:int):

    solved = mark_problem_solved(problem_id)

    if solved:
        return {"message": "Problem marked as solved"}

    raise HTTPException(
        status_code=404,
        detail="Problem not found"
    )


@app.get("/reviews", tags=["Reviews"])
def reviews():

    return get_review_history()

@app.get("/reviews/overdue", tags=["Reviews"])
def overdue_reviews():

    return get_today_reviews()

@app.get("/reviews/today", tags=["Reviews"])
def today_reviews():

    return get_today_reviews()


@app.get("/stats", tags=["Statistics"])
def stats():

    return get_stats()