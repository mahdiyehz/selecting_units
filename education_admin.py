import logging
from user import User
from course import Course
from student import Student

logging.basicConfig(level=logging.INFO,
                    filename='selecting_units.log',
                    filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')


class EducationAdmin(User):

    def show_all_units(self):
        total_units = 0
        for course in Course.courses_file.read_file():
            unit_num = int(course['unit number'])
            total_units += unit_num
        print(f'number of total units is: {total_units}')

    def show_student_list_course(self):
        course_name = input("Enter course name: ")
        for row in Course.courses_file.read_file():
            if row["course name"] == course_name:
                student_list = eval(row["student list"])
                for student in student_list:
                    print(student)
                    print("_____________________")

    def show_student_list(self):
        for row in Student.student_file.read_file():
            student_name = row["username"]
            student_id = row["student id"]
            print(f"{student_name}, {student_id}")
            print("___________________________")

    def search_student(self):
        choice = int(input("What do you want to search for?\n1. student name\n2. student id\n>>>? "))
        if choice == 1:
            student_name = input("Enter student name: ")
            student_info = Student.student_file.find_row_item("username", student_name)
            return eval(student_info["course"])
            # if student_info:
            #     print(f'student name:{student_info["username"]}\nstudent id:{student_info["student id"]}\ncourses list: {eval(student_info["course"])}')
            # else:
            #     print("This student not exist!")
        elif choice == 2:
            student_id = input("Enter student id: ")
            student_info = Student.student_file.find_row_item("student id", student_id)
            return eval(student_info["course"])
            # if student_info:
            #     print(
            #         f'student name:{student_info["username"]}\nstudent id:{student_info["student id"]}\ncourses list: {eval(student_info["course"])}')
            # else:
            #     print("This student not exist!")
        else:
            print(f'{choice}is not a valid choice!')
            logging.warning("invalid choice")

    def display_student_courses(self):
        student_name = input("Enter student name: ")
        student_info = Student.student_file.find_row_item("username", student_name)
        student_course_list = eval(student_info["course"])
        for course in student_course_list:
            print(f'course name: {course["course name"]}\ncourse professor: {course["professor name"]}\nunit number:{course["number of units"]}')
            print("_______________________________________")

    def confirmation_selecting_unit(self):
        student_name = input("Enter student name")
        action = int(input("What do you want?\n1. accept selecting unit\n2. reject selecting unit"))
        student_info = Student.student_file.find_row_item("username", student_name)
        if action == 1:
            Student.student_file.edit_status(student_info["username"], 1)
            logging.info("selecting unit accepted!")
        elif action == 2:
            Student.student_file.edit_status(student_info["username"], 2)
            for course in eval(student_info["course"]):
                Course.courses_file.edit_course_capacity(course["course name"], "add")
                logging.info("selecting unit rejected!")
        else:
            print(f'{action}is not a valid choice!')
            logging.warning("invalid choice")

    @staticmethod
    def display_admin_menu():
        print("""
        
_*Education Admin Menu*_
1. Show courses list
2. Search in courses
3. Show number of total units
4. Define new course
5. Show student list by course name
6. Show student list
7. Search student
8. Select student and display them course
9. accept or reject student courses 
10. Quit
        """)

    def education_admin_menu(self):
        choice = 0
        while choice != 10:
            super().print_role()
            self.display_admin_menu()
            choice = int(input("Enter an option: "))
            if choice == 1:
                Course.show_courses_list()
            elif choice == 2:
                Course.search_courses()
            elif choice == 3:
                self.show_all_units()
            elif choice == 4:
                Course.define_new_course()
            elif choice == 5:
                self.show_student_list_course()
            elif choice == 6:
                self.show_student_list()
            elif choice == 7:
                self.search_student()
            elif choice == 8:
                self.display_student_courses()
            elif choice == 9:
                self.confirmation_selecting_unit()
            elif choice == 10:
                break
            else:
                print(f'{choice}is not a valid choice!')
                logging.warning("invalid choice")
                