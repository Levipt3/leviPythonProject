username = ["admin", "user1", "user2"]
password = ["123", "123", "123"]


def register():
    print("Welcome to ATM")
    print("Enter your details to register")
    name = input("Username: ")
    if name in username:
        print("Username already exists")
        return False
    else:
        word = input("Password: ")
        if len(word) < 6:
            print("Password must be at least 6 characters")
            return False
        else:
            username.append(name)
            password.append(word)
            print("Registration successful")
            return True


def login():
    print("Enter your details to login")
    name = input("Username: ")
    word = input("Password: ")
    if name in username and word in password:
        print("Login successful")
        return True
    else:
        print("Invalid username or password")
        return False


if __name__ == '__main__':
    if register():
        login()

