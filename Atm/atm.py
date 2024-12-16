current_user_index = None  # 当前用户索引，初始化为None表示未登录

# 注册用户列表
users_list = [
    {'username': 'admin', 'password': '123456', 'balance': 3000},
    {'username': 'liuli', 'password': '123456', 'balance': 2000},
    {'username': 'liu', 'password': '123456', 'balance': 1000},
]


# 检查用户名和密码的有效性
def is_valid_user(name, password):
    return any(name == user['username'] and password == user['password'] for user in users_list)


# 注册新用户的函数
def register():
    print("--欢迎来到ATM系统--")
    while True:
        print("--请输入您的注册信息--")
        name = input("用户名[register/exit]: ")
        if name == "exit":
            print("--信息: 感谢您的注册--")
            break

        if any(name == user['username'] for user in users_list):
            print("--信息: 用户名已被使用--")
            continue

        word = input("密码[register/exit]: ")
        if word == "exit":
            print("--信息: 感谢您的注册--")
            break

        if len(word) < 6:
            print("--错误信息: 密码必须至少6个字符--")
            continue

        users_list.append({'username': name, 'password': word, 'balance': 3000})
        print("--信息: 注册成功--")
        return  # 直接返回以返回到主菜单


# 登录到ATM的函数
def login():
    global current_user_index
    while True:
        print("--信息: 输入您的登录信息--")
        name = input("用户名[login/exit]: ")
        word = input("密码[login/exit]: ")

        if name == "exit" or word == "exit":
            print("--信息: 感谢您使用ATM--")
            break

        if is_valid_user(name, word):
            current_user_index = next(index for index, user in enumerate(users_list) if user['username'] == name)
            print("--信息: 登录成功--")
            return

        print("--错误信息: 无效的用户名或密码--")


# 检查用户余额的函数
def check_balance():
    if current_user_index is None:
        print("--错误信息: 请先登录以查看余额--")
    else:
        balance = users_list[current_user_index]['balance']
        print("--信息: 您的余额是: $" + str(balance) + "--")


# 取款的函数
def withdraw():
    if current_user_index is None:
        print("--错误信息: 请先登录以进行取款--")
    else:
        balance = users_list[current_user_index]['balance']
        while True:
            try:
                amount = int(input("请输入取款金额: "))
                if amount > balance:
                    print("--错误信息: 余额不足--")
                    continue
                users_list[current_user_index]['balance'] -= amount
                print("--信息: 您已成功取款 $" + str(amount) + "--")
                break
            except ValueError:
                print("--错误信息: 请输入数字--")


# 存款的函数
def deposit():
    if current_user_index is None:
        print("--错误信息: 请先登录以进行存款--")
    else:
        while True:
            try:
                amount = int(input("请输入存款金额: "))
                users_list[current_user_index]['balance'] += amount
                print("--信息: 您已成功存款 $" + str(amount) + "--")
                break
            except ValueError:
                print("--错误信息: 请输入数字--")


# 转账的函数
def transfer():
    if current_user_index is None:
        print("--错误信息: 请先登录以进行转账--")
    else:
        while True:
            try:
                to_user = input("请输入转账对象用户名: ")
                if to_user == "admin":
                    print("--错误信息: 不能转账给管理员--")
                    continue
                if to_user not in [user['username'] for user in users_list]:
                    print("--错误信息: 无效的用户名--")
                    continue
                amount = int(input("请输入转账金额: "))
                if amount > users_list[current_user_index]['balance']:
                    print("--错误信息: 余额不足--")
                    continue
                users_list[current_user_index]['balance'] -= amount
                users_list[next(index for index, user in enumerate(users_list) if user['username'] == to_user)]['balance'] += amount
                print("--信息: 您已成功转账 $" + str(amount) + " 给 " + to_user + "--")
                break
            except ValueError:
                print("--错误信息: 请输入数字--")


# 退卡的函数
def logout():
    global current_user_index
    current_user_index = None
    print("--信息: 您已成功退卡--")


def get_menu():
    menu = """
    ***********************欢迎来到LaATM***************************
    ***********************请选择操作选项***************************
    ****** 1.注册 2.登录 3.余额查询 4.取款 5.存款 6.转账 7.退卡 *******
    """
    while True:
        print(menu)
        try:
            choice = int(input("请输入您的选择: "))
        except ValueError:
            print("--错误: 输入无效，请输入数字--")
            continue

        if choice == 1:
            register()
        elif choice == 2:
            login()
        elif choice == 3:
            check_balance()
        elif choice == 4:
            withdraw()
        elif choice == 5:
            deposit()
        elif choice == 6:
            transfer()
        elif choice == 7:
            logout()
        else:
            print("--无效选择--")


# 主函数运行ATM
if __name__ == '__main__':
    get_menu()
