import sys
import logging
from user import User
from student import Student
from professor import Professor
from education_admin import EducationAdmin

logging.basicConfig(level=logging.INFO,
                    filename='selecting_units.log',
                    filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')


class MainMenu:
    """Display a menu and respond to choices when run."""

    def __init__(self):
        self.role = None
        self.choices = {
            "1": self.registration,
            "2": self.login_to_account,
            "3": self.quit
        }

    @staticmethod
    def display_menu():
        print("""
*Menu*

1. Registration
2. Login to account
3. Quit
        """)

    def run_main(self):
        """Display the menu and respond to choices."""
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f'{choice}is not a valid choice!')
                logging.warning("invalid choice")

    def registration(self):
        while True:
            try:
                self.role = self.role_validation(
                input("Define your role:\n1. Student\n2. Professor\n3. Education Admin\n>>>? "))
            except Exception as e:
                print(e)
                continue
            break

        if self.role == "1":
            Student.registration()
        elif self.role == "2":
            Professor.registration()
        elif self.role == "3":
            EducationAdmin.registration()

    def login_to_account(self):
        user_info = User.login_to_account()
        if user_info:
            if self.role == "1":
                student = Student(user_info["username"], user_info["password"])
                student.student_menu()
            elif self.role == "2":
                professor = Professor(user_info["username"], user_info["password"])
                professor.professor_menu()
            elif self.role == "3":
                education_admin = EducationAdmin(user_info["username"], user_info["password"])
                education_admin.education_admin_menu()

    @staticmethod
    def quit():
        sys.exit(0)

    @staticmethod
    def role_validation(role):
        if role not in ["1", "2", "3"]:
            logging.warning("Invalid role!")
            raise Exception("Invalid role!just enter a number between 1-3")
        else:
            return role


MainMenu().run_main()
