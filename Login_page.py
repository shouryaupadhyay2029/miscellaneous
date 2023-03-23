import re
import bcrypt
import time
from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(app, default_limits=["1000 per day", "100 per hour"])
limiter.key_func = get_remote_address

@app.route("/")
@limiter.limit("10 per minute")

def write_database(username, hashed_password):
    with open("/home/piyush/Desktop/Code/coading/python/Database.txt", "a") as f:
        f.write(f"{username}|{hashed_password.decode('utf-8')}\n")


def read_database():
    database = {}
    with open("/home/piyush/Desktop/Code/coading/python/Database.txt", "r") as f:
        for line in f:
            fields = line.strip().split("|")
            if len(fields) == 2: 
                username, hashed_password = fields 
                database[username] = hashed_password.encode('utf-8')
    return database

LOGIN_ATTEMPTS = {}  # a dictionary to store the number of login attempts for each user

def login(database):
    print("Login Page")
    while True:
        username_input = input("Input Username: ").strip()
        password_input = input("Input Password: ").strip()
        if username_input in database:
            hashed_password = database[username_input]
            if bcrypt.checkpw(password_input.encode('utf-8'), hashed_password):
                print("User logged in successfully")
                break
            else:
                print("Incorrect password")
                # increment the login attempt counter for this user
                LOGIN_ATTEMPTS[username_input] = LOGIN_ATTEMPTS.get(username_input, 0) + 1
                # check if the user has exceeded the maximum number of login attempts
                if LOGIN_ATTEMPTS.get(username_input, 0) >= 3:
                    print("Too many failed login attempts. Please try again later.")
                    # wait for 1 minute before allowing another login attempt
                    time.sleep(60)
        else:
            print("Invalid username")


def create_account(database):
    print("Create your account")
    while True:
        username = input("Input Username: ")
        if not re.match("^[a-zA-Z0-9_]+$", username):
            print("Username must only contain letters, numbers, or underscores")
        elif username in database:
            print("This username is already taken")
        else:
            break

    while True:
        password = input("Input Password: ")
        if not re.match("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", password):
            print("Password must be at least 8 characters long and contain at least one letter and one number")
        else:
            break

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    write_database(username, hashed_password)
    print(f"User {username} created successfully.")

database = read_database()
def get_start():
    database = read_database()
    while True:
        choice = input('login or signup: ')
        if choice == "login":
            login(database)
            break
        elif choice == "signup":
            create_account(database)
            login(database)
            break
        else: 
            print("Sorry, I didn't get that (use lowercase):")
if __name__ == "__main__":
    get_start()
