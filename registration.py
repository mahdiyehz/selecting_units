import logging
import hashlib
from file_Handler import FileHandler
from random import randint

logging.basicConfig(filename='selecting_units.log',
                    filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')


class Register:
    def __init__(self):
        self.role = input("Define your role:\n1. Student\n2. Professor\n3. Education director\n>>>? ")
        self.username = input("username: ")
        self.password = input("password: ")
        self.student_number = None

        # repeated password validity
        try:
            self.repeat_password = self.repeat_pw_validation(input("repeat_password: "))
        except Exception as e:
            print(e)

        # defining students id
        if self.role == "1":
            while True:
                try:
                    self.student_id()
                except Exception as e:
                    print(e)
                    continue
                break

        # hashing password and adding username and password into 'registered_users' file
        pw = self.repeat_password.encode()
        hashed_pw = hashlib.sha256(pw).hexdigest()
        dict_file = {'username': self.username, 'password': hashed_pw}
        filename = FileHandler('registered_users.csv')
        filename.add_to_file(dict_file)

    def repeat_pw_validation(self, repeat_password):
        if repeat_password != self.password:
            logging.error("repeated password isn't same to password")
            raise Exception("repeated password isn't same to password")
        else:
            return repeat_password

    def student_id(self):
        entrance_year = str(input("Enter your entrance year to university (e.g. 97): "))
        if len(entrance_year) != 2 or not isinstance(int(entrance_year), int):
            logging.error("entrance year format isn't true!")
            raise Exception("entrance year format isn't true!")
        else:
            self.student_number = entrance_year + ''.join([f'{(randint(0, 9))}' for i in range(0, 6)])
            print(self.student_number)
            return self.student_number
