import sqlite3
from faker import Faker

# Initialize Faker for generating sample data
fake = Faker()

def insert_sample_data():
    conn = sqlite3.connect('social_platform.db')
    cursor = conn.cursor()


    # show the tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    print("Tables in the database:")
    for table in tables:
        print(table[0])

    # Drop all the existing tables
    

    for table in tables:
        # sqlite_sequence
        if table[0] == 'sqlite_sequence':
            continue
        cursor.execute(f"DROP TABLE IF EXISTS {table[0]};")
    conn.commit()

    # execute the SQL file 
    with open('export_schema.sql', 'r') as f:
        cursor.executescript(f.read())
    conn.commit()
    # Create tables   

  

    # Insert 200,000 users

    # Ensure unique usernames
    usernames = set()
    while len(usernames) < 1000000:
        usernames.add(fake.user_name())

    print('Inserting data...')
    cursor = conn.cursor()
    # Ensure unique emails
    emails = set()
    while len(emails) < 1000000:
        emails.add(fake.email())
    users = [(username, email, fake.password()) for username, email in zip(usernames, emails)]

    print('Inserting users...')
  
    cursor.executemany("INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?);", users)
    cursor.execute("SELECT * FROM users;")
    users = cursor.fetchall()



    print('Inserting posts...')
    # Insert 200,000 posts
    posts = [(fake.random_int(min=1, max=1000000), fake.text(max_nb_chars=200)) for _ in range(1000000)]
    cursor.executemany("INSERT INTO posts (user_id, content) VALUES (?, ?);", posts)

    print('Inserting comments...')
    # Insert 200,000 comments
    comments = [(fake.random_int(min=1, max=1000000), fake.random_int(min=1, max=1000000), fake.text(max_nb_chars=200)) for _ in range(1000000)]
    cursor.executemany("INSERT INTO comments (post_id, user_id, content) VALUES (?, ?, ?);", comments)

    print('Inserting likes...')
    # Insert 200,000 likes
    likes = [(fake.random_int(min=1, max=1000000), fake.random_int(min=1, max=1000000)) for _ in range(1000000)]
    cursor.executemany("INSERT INTO likes (post_id, user_id) VALUES (?, ?);", likes)

    print('Inserting friendships...')
    # Insert 200,000 friendships
    friendships = [(fake.random_int(min=1, max=1000000), fake.random_int(min=1, max=1000000)) for _ in range(1000000)]
    cursor.executemany("INSERT INTO friendships (user_id, friend_id) VALUES (?, ?);", friendships)

    print('Inserting messages...')
    # Insert 200,000 messages
    messages = [(fake.random_int(min=1, max=1000000), fake.random_int(min=1, max=1000000), fake.text(max_nb_chars=200)) for _ in range(1000000)]
    cursor.executemany("INSERT INTO messages (sender_id, receiver_id, content) VALUES (?, ?, ?);", messages)

    print('Data insertion complete.')
    conn.commit()

#   show the tables and count of each table

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables in the database:")
    for table in tables:
        cursor.execute(f"SELECT COUNT(*) FROM {table[0]};")
        count = cursor.fetchone()[0]
        print(f"{table[0]}: {count}")

    conn.close()


if __name__ == "__main__":
    insert_sample_data()