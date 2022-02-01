import logging
import hashlib
import os
from file_Handler import FileHandler

logging.basicConfig(level=logging.INFO,
                    filename='selecting_units.log',
                    filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')


class User:
    users_file = FileHandler("registered_users.csv")

    def __init__(self, username, password):
        self.username = username
        self.password = password

    # register new user
    @classmethod
    def registration(cls):
        # username input
        username = None
        while True:
            try:
                if os.path.isfile("registered_users.csv"):
                    username = cls.username_validation()
                else:
                    username = username = input("username: ")
            except Exception as e:
                print(e)
                continue
            break

        # repeated password validity
        password = None
        try:
            password = cls.repeat_pw_validation()
        except Exception as e:
            print(e)
        hashed_pw = cls.hashing_pw(password)
        User.users_file.add_to_file({"username": username, "password": hashed_pw})
        logging.info("new user registered!")
        print("registration was successfully!")

    # login to existing user account
    @classmethod
    def login_to_account(cls):
        # user  and password input for login
        input_username = None
        input_password = None
        try:
            input_username = cls.input_username_checking(input('Enter your username: '))
            if input_username:
                while True:
                    try:
                        input_password = cls.input_password_checking(input_username, input("Enter your password: "))
                        logging.info("login successfully!")
                    except Exception as e:
                        print(e)
                        continue
                    break
        except Exception as e:
            print(e)
            # MainMenu().run_main()
        user_info = {"username": input_username, "password": input_password}
        return user_info

    # print role
    @classmethod
    def print_role(cls):
        print(f"your role:{cls.__name__}")

    # checking username validation
    @staticmethod
    def username_validation():
        username = input("username: ")
        for user in User.users_file.read_file():
            if username == user['username']:
                raise Exception("this username already exists! enter another username")
        return username

    # checking repeated password validation
    @staticmethod
    def repeat_pw_validation():
        password, repeat_password = input("password: "), input("repeat_password: ")
        if repeat_password != password:
            logging.error("repeated password isn't same to password")
            raise Exception("repeated password isn't same to password")
        else:
            return password

    # hashing password
    @staticmethod
    def hashing_pw(password):
        pw = password.encode()
        hashed_pw = hashlib.sha256(pw).hexdigest()
        return hashed_pw

    # checking input username for login
    @staticmethod
    def input_username_checking(input_username):
        user_info = User.users_file.find_row_item("username", input_username)
        if not user_info:
            logging.error("this account dose not exist!")
            raise Exception("this account dose not exist!")
        return input_username

    # checking input password for login
    @staticmethod
    def input_password_checking(input_username, input_password):
        hashed_pw = User.hashing_pw(input_password)
        info_user = User.users_file.find_row_item("username", input_username)
        if info_user['password'] != hashed_pw:
            logging.error("wrong password! login unsuccessfully")
            raise Exception("wrong password!")
        else:
            return hashed_pw
