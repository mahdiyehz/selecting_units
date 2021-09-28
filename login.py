import logging
import sys
import hashlib
from file_Handler import FileHandler
from student_access import StudentMenu
from education_director_access import EducationDirectorMenu

logging.basicConfig(level=logging.INFO,
                    filename='selecting_units.log',
                    filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')

# Todo: add professor role


class LoginToAccount:
    def __init__(self):
        self.users_file = FileHandler('registered_users.csv')
        self.read_users_file = self.users_file.read_file()
        self.students_file = FileHandler("students_info.csv")
        self.read_student_file = self.students_file.read_file()
        self.input_user_name = None
        self.input_password = None
        # user  and password input for login
        try:
            if self.username_checking():
                while True:
                    try:
                        self.password_checking()
                        logging.info("login successfully!")
                    except Exception as e:
                        print(e)
                        continue
                    break
        except Exception as e:
            print(e)
            sys.exit(0)

        self.log_in()

    def password_checking(self):
        self.input_password = input("Enter your password: ")
        input_pw = self.input_password.encode()
        hashed_input_pw = hashlib.sha256(input_pw).hexdigest()
        for user in self.read_users_file:
            if user['username'] == self.input_user_name:
                if user['password'] != hashed_input_pw:
                    logging.error("wrong password! login unsuccessfully")
                    raise Exception("wrong password!")

    def username_checking(self):
        self.input_user_name = input('Enter your username: ')
        find = False
        for user in self.read_users_file:
            if self.input_user_name == user['username']:
                find = True
                return find
        if not find:
            logging.error("this account dose not exist!")
            raise Exception("this account dose not exist!")

    def log_in(self):
        student_find = False
        for user in self.read_student_file:
            if self.input_user_name == user['username']:
                print("Student")
                StudentMenu().run_student()
                student_find = True

        if not student_find:
            print("Education Director")
            EducationDirectorMenu().run_director()
