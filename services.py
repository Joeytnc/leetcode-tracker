import sqlite3
from http.client import HTTPException


def add_problem(title, difficulty, topic):
    # Connect to database
    conn = sqlite3.connect("problems.db")
    # Create cursor object
    cursor = conn.cursor()

    # Insert a new problem
    cursor.execute("""
    INSERT INTO problems(
        title,
        difficulty,
        topic,
        solved
    )
    Values (?, ?, ?, ?)
    """,(
        title,
        difficulty,
        topic,
        0
    ))

    conn.commit()
    conn.close()

def get_all_problems():
    conn = sqlite3.connect("problems.db")
    cursor = conn.cursor()

    # Get all problems
    cursor.execute("SELECT * FROM problems")
    # Fetch all rows from query result
    rows = cursor.fetchall()
    # Close
    conn.close()

    return rows

def get_problem_by_id(problem_id):
    conn = sqlite3.connect("problems.db")
    cursor = conn.cursor()

    # Get one problem by id
    cursor.execute(
        "SELECT * FROM problems WHERE id = ?",
        (problem_id,)
    )
    problem = cursor.fetchone()
    conn.close()

    return problem

def update_problem_by_id(problem_id, title, difficulty, topic):
    conn = sqlite3.connect("problems.db")
    cursor = conn.cursor()

    # Update problem by id
    cursor.execute("""
    UPDATE problems
    SET title = ?,
        difficulty = ?,
        topic = ?
    WHERE id = ?
    """,(
        title,
        difficulty,
        topic,
        problem_id

    ))

    # Check if any row was updated
    if cursor.rowcount == 0:
        conn.close()
        return None

    conn.commit()
    conn.close()

    return True

def delete_problem_by_id(problem_id):
    conn = sqlite3.connect("problems.db")
    cursor = conn.cursor()

    # Delete problem by id
    cursor.execute(
        "DELETE FROM problems WHERE id = ?",
        (problem_id,)
    )

    # Check if any row was deleted
    if cursor.rowcount == 0:
        conn.close()
        return None

    conn.commit()
    conn.close()

    return True

def get_stats():
    conn = sqlite3.connect("problems.db")
    cursor = conn.cursor()

    # Count all problems
    cursor.execute("SELECT COUNT(*) FROM problems")

    total = cursor.fetchone()[0]

    # Easy problems count
    cursor.execute("SELECT COUNT(*) FROM problems WHERE difficulty = ?",
                   ("Easy",)
                   )
    easy = cursor.fetchone()[0]

    # Medium problems count
    cursor.execute("SELECT COUNT(*) FROM problems WHERE difficulty = ?",
                   ("Medium",)
                   )
    medium = cursor.fetchone()[0]

    # Hard problems count
    cursor.execute("SELECT COUNT(*) FROM problems WHERE difficulty = ?",
                   ("Hard",)
                   )
    hard = cursor.fetchone()[0]

    conn.close()

    return {
        "total": total,
        "easy": easy,
        "medium": medium,
        "hard": hard

    }