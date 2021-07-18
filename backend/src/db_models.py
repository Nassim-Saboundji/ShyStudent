from database import Database

# Run this file once to create the required table inside your postgres database.
db = Database()

db.exec(""" 
CREATE TABLE users(
    username VARCHAR PRIMARY KEY,
    password bytea,
    type VARCHAR
)
""",())

db.exec("""
CREATE TABLE rooms(
    name VARCHAR PRIMARY KEY,
    owner_name VARCHAR,
    FOREIGN KEY (owner_name) REFERENCES users(username) ON DELETE CASCADE
)
 """, ())

db.exec("""
 CREATE TABLE questions(
     question VARCHAR PRIMARY KEY,
     status VARCHAR,
     asker_name VARCHAR,
     FOREIGN KEY (asker_name) REFERENCES users(username) ON DELETE CASCADE
 )
""",())

db.close()