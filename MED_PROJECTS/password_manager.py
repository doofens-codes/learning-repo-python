from cryptography.fernet import Fernet

"""def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)"""


def load_key():
    file = open("key.key", "rb")
    key_data = file.read()
    file.close()
    return key_data


def view():
    with open("passwords.txt", "r") as p:
        for line in p.readlines():
            curLine = line.strip()
            userN, passW = curLine.split("/")
            print(
                f"Username: {userN}; Password: {fer.decrypt(passW.encode()).decode()}"
            )


def add():
    name = input("Username: ")
    pwd = input("Password: ")
    with open("passwords.txt", "a") as p:
        p.write(name + "/" + fer.encrypt(pwd.encode()).decode() + "\n")


mPwd = input("Enter your master password: ")
mKey = load_key() + mPwd.encode()
fer = Fernet(mKey)

while True:
    entryMode = (
        input(
            "add - To add a new password/view - To view stored passwords/ q or Q to quit:"
        )
        .lower()
        .strip()
    )

    if entryMode == "q":
        break

    if entryMode == "view":
        view()
    elif entryMode == "add":
        add()
