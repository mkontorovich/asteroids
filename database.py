import sqlite3

def create_table():
    conn = sqlite3.connect('high_scores.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS high_scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        player_name TEXT NOT NULL,
        score INTEGER NOT NULL,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
    ''')
    conn.commit()
    conn.close()

def print_scores():
    conn = sqlite3.connect('high_scores.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM high_scores')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

def add_high_score(player_name, score):
    conn = sqlite3.connect('high_scores.db')
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM high_scores')
    count = cursor.fetchone()[0] # Access the first element of the tuple

    if count >= 5:
        cursor.execute('''
            DELETE FROM high_scores
            WHERE id = (
                SELECT id FROM high_scores
                ORDER BY score ASC, date ASC
                LIMIT 1
            )
        ''')

    cursor.execute('''
        INSERT INTO high_scores (player_name, score)
        VALUES (?, ?)
    ''', (player_name, score))
    conn.commit()
    conn.close()

# If limit is provided, it will return that many top scores.
# If limit is omitted and all_top=True, it returns all scores tied for the top score.
# If both limit and all_top are omitted, it returns the single top score.
def get_top_scores(limit=None, all_top=False):
    with sqlite3.connect('high_scores.db') as conn:
        cursor = conn.cursor()

        if all_top:
            # Find the maximum score first
            cursor.execute('SELECT MAX(score) FROM high_scores')
            top_score = cursor.fetchone()[0]
            
            # Retrieve all entries with this top score
            cursor.execute('''
            SELECT player_name, score, date
            FROM high_scores
            WHERE score = ?
            ORDER BY date ASC
            ''', (top_score,))
            return cursor.fetchall()
        
        elif limit is not None:
            # Retrieve the specified number of top scores
            cursor.execute('''
            SELECT player_name, score, date
            FROM high_scores
            ORDER BY score DESC
            LIMIT ?
            ''', (limit,))
            return cursor.fetchall()
        
        else:
            # Retrieve only the very top score if no limit or all_top specified
            cursor.execute('''
            SELECT player_name, score, date
            FROM high_scores
            ORDER BY score DESC
            LIMIT 1
            ''')
            return cursor.fetchone()