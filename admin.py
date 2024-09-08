from users import login

def deleteAccount(users):
    # Ensure the user is logged in and has admin rights
    role = login(users)
    if role != "admin":
        print("You need to be an admin to delete accounts.")
        return

    deleteAccountName = input("What account do you want to delete? ")
    userFound = False
    updated_users = []

    for user in users:
        if deleteAccountName == user["username"]:
            userFound = True
            print(f"{user['username']} has been deleted.")
        else:
            updated_users.append(user)

    if userFound:
        # Update the file with the remaining users
        with open('users.txt', 'w') as f:
            for user in updated_users:
                f.write(f"{user['username']}, {user['password']}, {user.get('role', 'user')}\n")
    else:
        print(f"User {deleteAccountName} has not been found.")

    # Update the users list
    users[:] = updated_users  # Modify the original list in-place
