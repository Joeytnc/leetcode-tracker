from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from services import (
    add_problem, get_all_problems, get_problem_by_id, update_problem_by_id, delete_problem_by_id,
    get_stats, review_problem_by_id, get_review_history, get_overdue_reviews
)

app = FastAPI()

class ProblemCreate(BaseModel):
    title: str
    difficulty: str
    topic: str

@app.get("/")
def root():

    return {"message": "LeetCode Tracker API running"}

@app.post("/problems/")
def create_problems(problem: ProblemCreate):

    add_problem(
        problem.title,
        problem.difficulty,
        problem.topic,
    )

    return {"message": "Problem added successfully"}

@app.get("/problems")
def get_problems():

    return get_all_problems()

@app.get("/problems/{problem_id}")
def get_problem(problem_id:int):

    problem = get_problem_by_id(problem_id)

    if problem:
        return problem
    raise HTTPException(
        status_code=404,
        detail="Problem not found"
    )

@app.put("/problems/{problem_id}")
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

@app.post("/problems/{problem_id}/review")
def review_problem(problem_id:int):

    reviewed = review_problem_by_id(problem_id)
    if reviewed:
        return {"message": "Problem reviewed successfully"}
    raise HTTPException(
        status_code=404,
        detail="Problem not found"
    )

@app.delete("/problems/{problem_id}")
def delete_problem(problem_id:int):

    deleted_problem = delete_problem_by_id(problem_id)
    if deleted_problem:
        return {"message": "Problem deleted successfully"}
    raise HTTPException(
        status_code=404,
        detail="Problem not found"
    )

@app.get("/stats")
def stats():

    return get_stats()

@app.get("/reviews")
def reviews():

    return get_review_history()

@app.get("/review_overdue")
def overdue_reviews():

    return get_overdue_reviews()

