import hashlib
import random
import os
import json


db_file = "users.db"

p = 23 
g = 5   


def save_user(username, hashed_password):
    if os.path.exists(db_file):
        try:
            with open(db_file, "r") as db:
                users = json.load(db)
        except json.JSONDecodeError:
            users = {}
    else:
        users = {}

    users[username] = hashed_password

    with open(db_file, "w") as db:
        json.dump(users, db)


def load_user(username):
    if os.path.exists(db_file):
        try:
            with open(db_file, "r") as db:
                users = json.load(db)
            return users.get(username, None)
        except json.JSONDecodeError:
            return None
    return None

def hash_password(password):
    hashed_password = int(hashlib.sha256(password.encode()).hexdigest(), 16)
    return hashed_password % p


def generate_challenge():
    challenge = random.randint(1, p-1)
    print(f"Server Challenge (c): {challenge}")
    return challenge


def generate_proof(challenge, secret):
    r = random.randint(1, p-1)
    print(f"User Random Value (r): {r}")
    
    t = pow(g, r, p)
    print(f"User Commitment (t): {t}")
    
    s = (r + challenge * secret) % (p-1)
    print(f"User Response (s): {s}")
    
    return t, s


def verify_proof(commitment, response, challenge, secret):
    lhs = pow(g, response, p)
    rhs = (commitment * pow(g, secret * challenge, p)) % p
    print(f"Verification LHS: {lhs}")
    print(f"Verification RHS: {rhs}")
    return lhs == rhs


def register(username, password):
    hashed_password = hash_password(password)
    save_user(username, hashed_password)
    print(f"User '{username}' registered successfully.")


def authenticate(username, password):
    stored_hashed_password = load_user(username)
    if stored_hashed_password is None:
        print(f"User '{username}' not found.")
        return False

    secret = hash_password(password)

    if secret != stored_hashed_password:
        print("Incorrect password.")
        return False

    challenge = generate_challenge()


    commitment, response = generate_proof(challenge, secret)

    if verify_proof(commitment, response, challenge, secret):
        print("Authentication successful!")
        return True
    else:
        print("Authentication failed!")
        return False

if __name__ == "__main__":
    print("Welcome to the ZKP Authentication System")
    choice = input("Do you want to (1) Register or (2) Authenticate? Enter 1 or 2: ")

    if choice == "1":
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        register(username, password)
    elif choice == "2":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        authenticate(username, password)
    else:
        print("Invalid choice. Exiting.")
