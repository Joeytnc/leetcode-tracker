import sqlite3
from datetime import date

def problem_to_dict(row):

    return {
        "id": row[0],
        "title": row[1],
        "difficulty": row[2],
        "topic": row[3],
        "solved": bool(row[4]),
        "review_count": row[5],
        "last_reviewed": row[6]

    }

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

    problems = []

    for row in rows:
        problems.append(
            problem_to_dict(row)
        )

    conn.close()

    return problems

def get_problem_by_id(problem_id):
    conn = sqlite3.connect("problems.db")
    cursor = conn.cursor()

    # Get one problem by id
    cursor.execute(
        "SELECT * FROM problems WHERE id = ?",
        (problem_id,)
    )
    problem = cursor.fetchone()

    if problem:
        return problem_to_dict(problem)

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

    # Solved problems count
    cursor.execute("SELECT COUNT(*) FROM problems WHERE solved = ?",
                   (1,)
                   )
    solved = cursor.fetchone()[0]

    conn.close()

    return {
        "total": total,
        "easy": easy,
        "medium": medium,
        "hard": hard,
        "solved": solved

    }

def review_problem_by_id(problem_id):
    conn = sqlite3.connect("problems.db")
    cursor = conn.cursor()

    # Increase review count
    # Update last reviewed date
    cursor.execute("""
    UPDATE problems
    SET review_count = review_count + 1,
        last_reviewed = ?
    WHERE id = ?
    
    """,(
        str(date.today()),
        problem_id
    ))

    # Check if any row was updated
    if cursor.rowcount == 0:
        conn.close()
        return None

    conn.commit()
    conn.close()

    return True

def get_review_history():
    conn = sqlite3.connect("problems.db")
    cursor = conn.cursor()

    # Get review information
    cursor.execute("""
    SELECT 
        id,
        title,
        review_count,
        last_reviewed
    FROM problems
    """)

    rows = cursor.fetchall()

    conn.close()

    reviews = []

    for row in rows:

        reviews.append({
            "id": row[0],
            "title": row[1],
            "review_count": row[2],
            "last_reviewed": row[3]

        })

    return reviews

def get_overdue_reviews():
    conn = sqlite3.connect("problems.db")
    cursor = conn.cursor()

    # Get review information
    cursor.execute("""
    SELECT
        id,
        title,
        review_count,
        last_reviewed
    FROM problems
    WHERE last_reviewed IS NOT NULL
    
    """)

    rows = cursor.fetchall()

    conn.close()

    overdue = []

    today = date.today()

    for row in rows:

        if row[3] is None:
            continue

        reviewed_date = date.fromisoformat(row[3])

        days_since_review = (today - reviewed_date).days

        if days_since_review >= 30:

            overdue.append({
                "id": row[0],
                "title": row[1],
                "review_count": row[2],
                "last_reviewed": row[3],
                "days_since_review": days_since_review

            })

    return overdue

def mark_problem_solved(problem_id):
    conn = sqlite3.connect("problems.db")
    cursor = conn.cursor()

    # Mark problem as solved
    cursor.execute("""
    UPDATE problems
    SET solved = 1
    WHERE id = ?
    
    """,(
        problem_id,
    ))

    # Check if any row was updated
    if cursor.rowcount == 0:
        conn.close()
        return None

    conn.commit()
    conn.close()

    return True

def get_problems_by_difficulty(difficulty):
    conn = sqlite3.connect("problems.db")
    cursor = conn.cursor()

    # Get problems by difficulty
    cursor.execute("""
    SELECT * FROM problems
    WHERE difficulty = ?
    """,(difficulty,)
                   )

    rows = cursor.fetchall()

    problems = []

    for row in rows:
        problems.append(
            problem_to_dict(row)
        )

    conn.close()

    return problems

def get_problem_by_topic(topic):
    conn = sqlite3.connect("problems.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM problems
    WHERE topic = ?
    """,(topic,)
                   )

    rows = cursor.fetchall()

    problems = []

    for row in rows:
        problems.append(
            problem_to_dict(row)
        )

    conn.close()

    return problems

def search_problems(keyword):
    conn = sqlite3.connect("problems.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM problems
    WHERE title LIKE ?
    """,(f"%{keyword}%",)
                   )

    rows = cursor.fetchall()

    problems = []
    for row in rows:
        problems.append(
            problem_to_dict(row)
        )

    conn.close()

    return problems