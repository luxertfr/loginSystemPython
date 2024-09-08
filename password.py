import bcrypt
from config import maxAttempts

def changePassword(username, users):
    attemptsMax = maxAttempts()  # Get maxAttempts from config
    user_found = False  # Track if the user was found

    for user in users:
        if user['username'] == username:
            user_found = True
            break

    if not user_found:
        print("User not found.")
        return

    for attemptReset in range(attemptsMax):
        currentPassword = input("Enter your current password: ")
        if bcrypt.checkpw(currentPassword.encode('utf-8'), user['password'].encode('utf-8')):
            newPassword = input("Enter your new password: ")
            hashedNewPassword = bcrypt.hashpw(newPassword.encode('utf-8'), bcrypt.gensalt())
            
            # Update the user's password in the list
            user['password'] = hashedNewPassword.decode('utf-8')
            
            # Update the file
            with open('users.txt', 'w') as f:
                for user in users:
                    f.write(f"{user['username']}, {user['password']}, {user.get('role', 'user')}\n")

            print("Password has been changed successfully!")
            break

        else:
            if attemptReset < attemptsMax - 1:
                print(f"Wrong current password. You have {attemptsMax - attemptReset - 1} attempts left.")
            else:
                print("Too many failed attempts. Please try again later.")
                break