import sqlite3

# Connect to database
conn = sqlite3.connect("problems.db")
# Create cursor object
cursor = conn.cursor()

# Create problems table if it's not exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS problems (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    difficulty TEXT NOT NULL,
    topic TEXT NOT NULL,
    solved INTEGER NOT NULL,
    review_count INTEGER DEFAULT 0,
    last_reviewed TEXT
    )
""")


# Save changes
conn.commit()

# Close database connection
conn.close()

print("Database initialized")
