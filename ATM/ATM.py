username = ["admin", "user1", "user2"]
password = ["123", "123", "123"]


def register():
    # username validation
    print("--Welcome to ATM--")
    while True:
        print("--Enter your details to register--")
        name = input("Username[register/exit]: ")
        # check if username is "exit" to exit the program
        if name == "exit":
            print("--Thank you for registering--")
            break
        if name in username:
            print("--Username already exists--")
        else:
            # password validation
            word = input("Password[register/exit]: ")
            if word == "exit":
                print("--Thank you for registering--")
                break
            # check if password is at least 6 characters long
            if len(word) < 6:
                print("--Password must be at least 6 characters--")
                return False
            else:
                username.append(name)
                password.append(word)
                print("--Registration successful--")
                return True


def login():
    while True:
        # login validation
        print("--Enter your details to login--")
        name = input("Username[login/exit]: ")
        word = input("Password[login/exit]: ")
        # check if username and password are valid
        if name == "exit" or word == "exit":
            print("--Thank you for using ATM--")
            break
        # check if username exists in the list
        if name in username:
            i = username.index(name)
            if word == password[i]:
                print("--Login successful--")
                break
            else:
                print("--Invalid username or password--")
                return False
        else:
            print("--Username orn password does not exists--")



if __name__ == '__main__':
    if register():
        login()

