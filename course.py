import logging
from file_Handler import FileHandler


logging.basicConfig(level=logging.INFO,
                    filename='selecting_units.log',
                    filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')


class Course:
    courses_file = FileHandler("courses_data.csv")

    def __init__(self, course_name, course_id, unit_number, capacity, professor_name=None):
        self.student_file = FileHandler("students_info.csv")
        self.course_name = course_name
        self.professor_name = professor_name
        self.unit_number = unit_number
        self.capacity = capacity
        self.course_id = course_id

    @classmethod
    def define_new_course(cls):
        course_name = input("course name: ")
        professor_name = input("professor name: ")
        unit_number = input("number of unit: ")
        capacity = int(input("capacity number: "))
        course_id = input("course id: ")
        course_info = {"course name": course_name, "professor name": professor_name,
                       "unit number": unit_number, "capacity": capacity, "course id": course_id, "student list": []}
        cls.courses_file.add_to_file(course_info)
        logging.info("new course defined successfully!")

    @staticmethod
    def show_courses_list():
        for course in Course.courses_file.read_file():
            for key, value in course.items():
                print("%s : %s" % (key, value))
            print('______________________________________')

    @staticmethod
    def search_courses():
        search_course_name = input("Enter course name: ")
        for course in Course.courses_file.read_file():
            if search_course_name == course['course name']:
                for key, value in course.items():
                    print('%s : %s' % (key, value))
                print('______________________________________')

    @staticmethod
    def show_all_units_admin():
        total_units = 0
        for course in Course.courses_file.read_file():
            unit_num = int(course['number of units'])
            total_units += unit_num
        print(f'number of total units is: {total_units}')
