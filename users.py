import bcrypt
from config import maxAttempts

def readUsersFromFile() :
    users = []
    try:
        with open('users.txt', 'r') as f:
            for line in f:
                username, password, admin = line.strip().split(', ')
                user = {"username": username, "password": password, "role": admin}
                users.append(user)
    except FileNotFoundError:
        # If the file doesn't exist, continue
        print("No existing users found, starting fresh.")
    return users

def saveUsersToFile(users) :
    with open('users.txt', 'w') as f:
        for user in users :
            f.write(f"{user['username']}, {user['password']}, {user['role']}\n")
                
                
def createAccount(users):
    newUsername = input("What username do you want? : ")
    newPassword = input("What password do you want? : ")

    # Username verification
    usernameTaken = False
    for user in users:
        if newUsername == user['username']:
            print("You need to use another username, this one is already used.")
            usernameTaken = True
            break  # Exit the loop if the username is found

    if usernameTaken:
        return  # Exit the function if the username is taken

    # Hashing 
    hashedPassword = bcrypt.hashpw(newPassword.encode('utf-8'), bcrypt.gensalt())

    newUser = {"username": newUsername, "password": hashedPassword.decode('utf-8'), "role": "user"}
    users.append(newUser)
    print(f"Account for {newUsername} created!")

    # Save the new user to the file
    saveUsersToFile(users)

def login(users):
    maxAttempts = 3
    for attempt in range(maxAttempts):
        username = input("What is your username? : ")
        password = input("What is your password? : ")

        for user in users:
            hashedPasswordFromFile = user['password'].encode('utf-8')
            if username == user['username'] and bcrypt.checkpw(password.encode('utf-8'), hashedPasswordFromFile):
                print("Welcome to your account!")
                return user['role']  # Return the role of the logged-in user

        if attempt < maxAttempts - 1:
            print(f"Wrong username or password. You have {maxAttempts - attempt - 1} attempts left.")
        else:
            print("Too many failed attempts. Please try again later.")
            break

    return None  # Return None if login fails after max attempts

