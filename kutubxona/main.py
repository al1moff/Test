# 1) database
# 2) model
# 3) UI
# 4) method

session_user : User = None

def register():
    d = {
        "name": input("Name:"),
        "username": input("Username:"),
        "password": input("Password:"),
    }
    user = User(**d)
    if user.check_username():
        print("Your username already exists!")
        return
    user.save_user()
    print("Registration successful !")


def login():
    global session_user

    d = {
        "username": input("Username:"),
        "password": input("Password:"),
    }

    obj = User(**d)
    session_user = obj.login_check()
    if not session_user:
        print("Wrong username or password !")
        return
    print(f"Welcome {session_user.name}")
    if session_user.role == "ADMIN":
        admin_menu()
    else:
        user_menu()


def category_crud():
    pass


def book_crud():
    pass


def settings():
    menu = """
    1) change info
    2) delete account
    3) <- back
    """
    key = int(input(menu))
    match key:
        case 1:
            menu_col = """
                1) name
                2) username
                3) password
                4) <- back
                    >>>"""
            key = int(input(menu_col))
            if key != 4:
                new_val = input("New value: ")
            match key:
                case 1:
                    session_user.change_info("name" , new_val)
                case 2:
                    session_user.change_info("username", new_val)
                case 3:
                    session_user.change_info("password", new_val)
                case 4:
                    settings()
            settings()

        case 2:
            if session_user.role == "ADMIN":
                admin_menu()
            else:
                user_menu()



def admin_menu():
    menu = """
    1) Category
    2) Book
    3) add admin
    4) settings
    5) logout
        >>>"""
    # C  create
    # R  remove
    # U  update
    # D  delete
    key = int(input(menu))
    match key:
        case 1:
            category_crud()
        case 2:
            book_crud()
        case 3:
            pass
        case 4:
            settings()
        case 5:
            return


def user_menu():
    pass


def UI():
    while True:
        text = """
        1) Register
        2) Login
        3) exit
            >>>"""
        key = int(input(text))
        match key:
            case 1:
                register()
            case 2:
                login()
            case 3:
                break


UI()


# class
"""
    AdminUI
    UserUI
    BookUI
    CategoryUI
    """