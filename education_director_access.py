import logging
import sys
from file_Handler import FileHandler

logging.basicConfig(level=logging.INFO,
                    filename='selecting_units.log',
                    filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')


# Todo: add number of remaining capacity in faze2


class EducationDirector:
    def __init__(self):
        self.course_name = None
        self.professor_name = None
        self.unit_number = None
        self.capacity = None
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

    def show_all_units(self):
        total_units = 0
        for course in self.read_course_file:
            unit_num = int(course['number of units'])
            total_units += unit_num
        print(f'number of total units is: {total_units}')

    def define_new_course(self):
        self.course_name = input("course name: ")
        self.professor_name = input("professor name: ")
        self.unit_number = input("number of unit: ")
        self.capacity = input("capacity number: ")
        courses_dict = {'course name': self.course_name, 'professor name': self.professor_name,
                        'number of units': self.unit_number, 'capacity': self.capacity}
        self.courses_file.add_to_file(courses_dict)
        logging.info("new course was registered!")


class EducationDirectorMenu:
    """Display a menu and respond to choices when run."""

    def __init__(self):
        self.education_director = EducationDirector()
        self.choices = {
            "1": self.view_courses_list,
            "2": self.search_in_courses,
            "3": self.view_total_units,
            "4": self.define_new_courses,
            "5": self.quit
        }

    @staticmethod
    def display_director_menu():
        print("""
*Education Director Menu*

1. Show courses list
2. Search in courses
3. Show number of total units
4. Define new course
5. Quit
        """)

    def run_director(self):
        """Display the menu and respond to choices."""
        while True:
            self.display_director_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f'{choice} is not a valid choice!')
                logging.warning("invalid choice")

    def view_courses_list(self):
        self.education_director.show_courses_list()

    def search_in_courses(self):
        self.education_director.search_courses()

    def view_total_units(self):
        self.education_director.show_all_units()

    def define_new_courses(self):
        self.education_director.define_new_course()

    def quit(self):
        sys.exit(0)



