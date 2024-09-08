# import bcrypt

# print("Welcome to this login system!")

# users = []

# # Read the users from the file users.txt
# try:
#     with open('users.txt', 'r') as f:
#         for line in f:
#             username, password, admin = line.strip().split(', ')
#             user = {"username": username, "password": password, "role": admin}
#             users.append(user)
# except FileNotFoundError:
#     # If the file doesn't exist, continue
#     print("No existing users found, starting fresh.")

# print(users)

# while True:
#     response = input("Do you want to create an account or login? ").lower()
#     usernameTaken = False
    
    
#     if response == "account":
#         newUsername = input("What username do you want? : ")
#         newPassword = input("What password do you want? : ")
#         # Username verification
#         for user in users:
#             if newUsername == user['username']:
#                 print("You need to use another username this one is already used.")
#                 usernameTaken = True
#                 break
            
#         if usernameTaken :
#             continue
        
#         # Hashing 
#         hashedPassword = bcrypt.hashpw(newPassword.encode('utf-8'), bcrypt.gensalt())

#         user = {"username": newUsername, "password": hashedPassword.decode('utf-8'), "role": "user"}
#         users.append(user)
#         print(f"Account for {newUsername} created!")
        
#         # Save in the file
#         with open('users.txt', 'a') as f:
#             f.write(f"{newUsername}, {hashedPassword.decode('utf-8')}, user\n")
        
#     elif response == "login":
#         successfulLogin = False
#         maxAttempts = 3
                
#         for attempt in range(maxAttempts):
#             username = input("What is your username? : ")
#             password = input("What is your password? : ")
            
#             for user in users:
#                 hashedPasswordFromFile = user['password'].encode('utf-8')
#                 if username == user['username'] and bcrypt.checkpw(password.encode('utf-8'), hashedPasswordFromFile):
#                     print("Welcome in your account!")
#                     successfulLogin = True
#                     break
            
#             if successfulLogin:
#                 while True: 
#                     resetPasswordResponse = input("Do you want to change your password? (yes/no): ").lower()
                    
#                     if resetPasswordResponse == "yes":
#                         for attemptReset in range(maxAttempts):
#                             currentPassword = input("Enter your current password: ")
#                             if bcrypt.checkpw(currentPassword.encode('utf-8'), hashedPasswordFromFile):
#                                 newPassword = input("Enter your new password: ")
#                                 hashedNewPassword = bcrypt.hashpw(newPassword.encode('utf-8'), bcrypt.gensalt())
                                
#                                 # Update the user's password in the list
#                                 for user in users:
#                                     if user['username'] == username:
#                                         user['password'] = hashedNewPassword.decode('utf-8')
                                        
                                
#                                 # Update the file
#                                 with open('users.txt', 'w') as f:
#                                     for user in users:
#                                         f.write(f"{user['username']}, {user['password']}, {user.get('role', 'user')}\n")
                                
#                                 print("Password has been changed successfully!")
#                                 break
                                
#                             else:
#                                 if attemptReset < maxAttempts - 1:
#                                     print(f"Wrong current password. You have {maxAttempts - attemptReset - 1} attempts left.")
#                                 else:
#                                     print("Too many failed attempts. Please try again later.")
#                                     break
                            
#                     elif resetPasswordResponse == "no":
#                         for user in users:
#                             admin = "admin"
#                             if admin == user["role"]:
#                                 delete = input("Do you want to delete account ? (yes)/(no) ").lower()
#                                 if delete == "yes" :
#                                     userFound = False
#                                     for user in users: 
#                                         deleteAccount = input("What account do you want to delete ? ")
#                                         if deleteAccount == user["username"] :
#                                             users.remove(user)
#                                             userFound = True
#                                             print(f"{user["username"]} has been deleted.")
#                                             with open('users.txt', 'w') as f:
#                                                 for user in users:
#                                                     f.write(f"{user['username']}, {user['password']}, {user.get('role', 'user')}\n")
#                                             break
#                                         else : 
#                                             print(f"User {deleteAccount} has not been found")
#                                 break
#                             else:
#                                 print("You are not admin")
#                                 successfulLogin = True
#                                 break
#                         break
                        
#                     else:
#                         print("Try to answer 'yes' or 'no'.")
#                     break
#                 break
            

        
#         if successfulLogin:
#             continue  # Continue the main loop after a succesful login

#     else:
#         print("Invalid response. Try to write 'account' or 'login'.")
        
#     # Leave or continue
#     cont = input("Do you want to continue? (yes/no): ").lower()
#     if cont != 'yes':
#         break

# for user in users:
#     print(f"Username: {user['username']}, Password: {user['password']}")
from users import readUsersFromFile, saveUsersToFile, createAccount, login
from admin import deleteAccount
from password import changePassword


def displayMenu() :
    print("\n--- Main Menu ---")
    print("1. Sign in")
    print("2. Login")
    print("3. Change password")
    print("4. Delete account (admin)")
    print("5. Leave")
    

def main():
    users = readUsersFromFile()
    while True:
        displayMenu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            createAccount(users)
        elif choice == "2":
            login(users)
        elif choice == "3":
            username = input("Enter your username: ")
            changePassword(username, users)
        elif choice == "4":
            deleteAccount(users)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Try to write the number properly")
    
    saveUsersToFile(users)

if __name__ == "__main__":
    main()