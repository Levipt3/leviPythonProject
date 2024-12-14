users = [
    ["admin", "123456"],
    ["jack", "123456"],
    ["leo", "123456"],
]

# Function to register a new user
def register():
    # username validation
    print("--Welcome to ATM System--")
    while True:
        print("--Enter your details to register--")
        name = input("Username[register/exit]: ")
        # check if username is "exit" to exit the program
        if name == "exit":
            print("--Info: Thank you for registering--")
            break
        for user in users:
            if name == user[0]:
                print("Info: Username is already in use.")
                break
        else:
            # password validation
            word = input("Password[register/exit]: ")
            if word == "exit":
                print("--Info: Thank you for registering--")
                break
            # check if password is at least 6 characters long
            if len(word) < 6:
                print("--Error info: Password must be at least 6 characters--")
                return False
            else:
                # add user to the list
                users.append([name, word])
                print("--Info: Registration successful--")
                return True


# Function to login to the ATM
def login():
    while True:
        # login validation
        print("--Info: Enter your details to login--")
        name = input("Username[login/exit]: ")
        word = input("Password[login/exit]: ")
        # check if username and password are valid
        if name == "exit" or word == "exit":
            print("--Info: Thank you for using ATM--")
            break
        # check if username and password exists in the list
        for user in users:
            if name == user[0] and word == user[1]:
                print("--Info: Login successful--")
                break
            else:
                print("--Error info: Invalid username or password--")
                break


def get_menu():
    menu = """
    ***********************欢迎来到LaATM***************************
    ***********************请选择操作选项***************************
    ******************* 1.注册 2.登录 3.退卡 ***********************
    """
    while True:
        print(menu)
        choice = int(input("Enter your choice: "))
        if choice == 1:
            register()
        elif choice == 2:
            login()
        elif choice == 3:
            print("--Thank you for using ATM--")
            break
        else:
            print("--Invalid choice--")


# Main function to run the ATM
if __name__ == '__main__':
    get_menu()
    if register():
        login()

