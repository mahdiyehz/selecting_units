import logging
import sys
from file_Handler import FileHandler

logging.basicConfig(level=logging.INFO,
                    filename='selecting_units.log',
                    filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')


# Todo: add number of remaining capacity in faze2

class Student:
    def __init__(self):
        self.selected_units_number = None
        self.courses_file = FileHandler('courses_data.csv')
        self.read_course_file = self.courses_file.read_file()

    def show_courses_list(self):
        for course in self.read_course_file:
            for key, value in course.items():
                print("%s : %s" % (key, value))
            print('************************')

    def search_courses(self):
        search_course_name = input("Enter course name: ")
        for course in self.read_course_file:
            if search_course_name == course['course name']:
                for key, value in course.items():
                    print('%s : %s' % (key, value))
                print('************************')

    # Todo: subtraction selected units from max units and raise exception when selected units lower than min units
    def show_all_units(self):
        min_unit = 10
        max_units = 20
        print(f'you can select units between {min_unit} and {max_units}')


class StudentMenu:
    """Display a menu and respond to choices when run."""

    def __init__(self):
        self.student = Student()
        self.choices = {
            "1": self.view_course_list,
            "2": self.search_courses,
            "3": self.view_total_unit,
            "4": self.quit
        }

    @staticmethod
    def display_student_menu():
        print("""
*Student Menu*

1. Show courses list
2. Search in courses
3. Show number of total units
4. Quit
        """)

    def run_student(self):
        """Display the menu and respond to choices."""
        while True:
            self.display_student_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f'{choice} is not a valid choice!')
                logging.warning("invalid choice")

    def view_course_list(self):
        self.student.show_courses_list()

    def search_courses(self):
        self.student.search_courses()

    def view_total_unit(self):
        self.student.show_all_units()

    def quit(self):
        sys.exit(0)



