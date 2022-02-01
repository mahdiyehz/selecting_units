import logging
import os
from user import User
from random import randint
from file_Handler import FileHandler
from course import Course

logging.basicConfig(level=logging.INFO,
                    filename='selecting_units.log',
                    filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')


class Student(User):
    student_file = FileHandler("students_info.csv")

    def __init__(self, username, password):
        super().__init__(username, password)
        self.min_unit = 10
        self.max_units = 20

    # register new student
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

        # defining students id
        student_id = None
        while True:
            try:
                student_id = cls.student_id()
            except Exception as e:
                print(e)
                continue
            break
        hashed_pw = cls.hashing_pw(password)
        User.users_file.add_to_file({"username": username, "password": hashed_pw})
        Student.student_file.add_to_file({"username": username, "student id": student_id, "course": [], "confirmation status": "waiting"})
        logging.info("new user registered!")

    # creating student's id
    @staticmethod
    def student_id():
        entrance_year = str(input("Enter your entrance year to university (e.g. 97): "))
        if len(entrance_year) != 2 or not isinstance(int(entrance_year), int):
            logging.error("entrance year format isn't true!")
            raise Exception("entrance year format isn't true!")
        else:
            student_number = entrance_year + ''.join([f'{(randint(0, 9))}' for i in range(0, 6)])
            print(f"your student_id is: {student_number}")
            return student_number

    def show_all_units(self):
        self.min_unit = 10
        self.max_units = 20
        print(f'you can select units between {self.min_unit} and {self.max_units}')

    def selecting_course(self):
        input_course_name = input("Enter course name you want to choose: ")
        selected_course_info = Course.courses_file.find_row_item("course name", input_course_name)
        if selected_course_info:
            if selected_course_info["capacity"] != "0":
                updated_course = {"username": self.username,
                                  "course": {"course name": selected_course_info["course name"],
                                             "professor name": selected_course_info["professor name"],
                                             "number of units": selected_course_info["unit number"]}}
                Student.student_file.edit_row(updated_course)
                Course.courses_file.edit_course_capacity(selected_course_info["course name"], "sub")
                Course.courses_file.add_student_to_course_list(selected_course_info["course name"], self.username)
                self.max_units -= 1
                print("course added successfully!")
                logging.info("course added successfully!")

    @staticmethod
    def display_student_menu():
        print("""

_*Student Menu*_
1. Show courses list
2. Search in courses
3. Show number of total units
4. Select course
5. Quit
        """)

    def student_menu(self):
        choice = 0
        while choice != 5:
            super().print_role()
            self.display_student_menu()
            choice = int(input("Enter an option: "))
            if choice == 1:
                Course.show_courses_list()
            elif choice == 2:
                Course.search_courses()
            elif choice == 3:
                self.show_all_units()
            elif choice == 4:
                try:
                    self.selecting_course()
                except Exception as e:
                    print(e)
                continue
            elif choice == 5:
                break
            else:
                print(f'{choice}is not a valid choice!')
                logging.warning("invalid choice")
