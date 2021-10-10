import logging
from user import User
from file_Handler import FileHandler
from course import Course

logging.basicConfig(level=logging.INFO,
                    filename='selecting_units.log',
                    filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')


class Professor(User):
    professor_file = FileHandler("professor_info.csv")

    def __init__(self, username, password):
        super().__init__(username, password)
        self.min_unit = 10
        self.max_unit = 15
        Professor.professor_file.add_to_file({"username": username, "course": []})
        for course in Course.courses_file.read_file():
            if course["professor name"] == self.username:
                Professor.professor_file.add_course_to_professor_file(self.username, course)

    def show_professor_courses(self):
        for course in Course.courses_file.read_file():
            if course["professor name"] == self.username:
                for key, value in course.items():
                    print('%s : %s' % (key, value))
                print('______________________________________')

    def select_course(self):
        input_course_name = input("Enter course name: ")
        selected_course = Course.courses_file.find_row_item("course name", input_course_name)
        if selected_course:
            if selected_course["professor name"] is None:
                updated_course = {"course name": selected_course["course name"],
                                  "professor name": self.username,
                                  "number of units": selected_course["unit number"]}
                Professor.professor_file.add_course_to_professor_file(self.username, updated_course)
                Course.courses_file.edit_course_professor(selected_course["course name"], self.username)

    def show_student_list_course(self):
        course_id = input("Enter course id: ")
        for row in Course.courses_file.read_file():
            if row["course id"] == course_id:
                student_list = eval(row["student list"])
                for student in student_list:
                    print(student)
                    print("_____________________")

    @staticmethod
    def display_professor_menu():
        print("""
        
_*Professor Menu*_
1. Show courses list
2. Search in courses
3. Show selected courses
4. Select course
5. Show selected course student list
6. Quit
        """)

    def professor_menu(self):
        choice = 0
        while choice != 5:
            super().print_role()
            self.display_professor_menu()
            choice = int(input("Enter an option: "))
            if choice == 1:
                Course.show_courses_list()
            elif choice == 2:
                Course.search_courses()
            elif choice == 3:
                self.show_professor_courses()
            elif choice == 4:
                self.select_course()
            elif choice == 5:
                self.show_student_list_course()
            elif choice == 6:
                break
            else:
                print(f'{choice}is not a valid choice!')
                logging.warning("invalid choice")
