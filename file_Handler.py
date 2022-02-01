import csv
from csv import DictWriter


class FileHandler:
    def __init__(self, file_path='data.csv'):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path, 'r') as myfile:
            reader = csv.DictReader(myfile)
            return list(reader)

    def add_to_file(self, new_value, mode="a"):
        if isinstance(new_value, dict):
            fields = new_value.keys()
            new_value = [new_value]
        elif isinstance(new_value, list):
            fields = new_value[0].keys()

        with open(self.file_path, mode, newline='') as myfile:
            writer = DictWriter(myfile, fieldnames=fields)
            if myfile.tell() == 0:
                writer.writeheader()
            writer.writerows(new_value)

    def edit_row(self, updated_dictionary):
        all_rows = self.read_file()
        final_row = []
        for row in all_rows:
            if row["username"] == updated_dictionary["username"]:
                l_x = eval(row["course"])
                l_x.append(updated_dictionary["course"])
                row["course"] = l_x
            final_row.append(row)
            self.add_to_file(final_row, mode="w")

    def edit_status(self, student_name, status):
        all_rows = self.read_file()
        final_row = []
        for row in all_rows:
            if row["username"] == student_name:
                if status == 1:
                    row["confirmation status"] = "accepted"
                else:
                    row["confirmation status"] = "rejected"
                    row["course"] = []
            final_row.append(row)
            self.add_to_file(final_row, mode="w")

    def edit_course_capacity(self, course_name, action):
        all_rows = self.read_file()
        final_row = []
        for row in all_rows:
            if row["course name"] == course_name:
                new_capacity = int(row["capacity"])
                if action == "sub":
                    row["capacity"] = new_capacity - 1
                elif action == "add":
                    row["capacity"] = new_capacity + 1
            final_row.append(row)
            self.add_to_file(final_row, mode="w")

    def add_student_to_course_list(self, course_name, student_name):
        all_rows = self.read_file()
        final_row = []
        for row in all_rows:
            if row["course name"] == course_name:
                l_x = eval(row["student list"])
                l_x.append(student_name)
                row["student list"] = l_x
            final_row.append(row)
            self.add_to_file(final_row, mode="w")

    def add_course_to_professor_file(self, professor_name, course_info):
        all_rows = self.read_file()
        final_row = []
        for row in all_rows:
            if row["username"] == professor_name:
                l_x = eval(row["course"])
                l_x.append(course_info)
                row["course"] = l_x
            final_row.append(row)
            self.add_to_file(final_row, mode="w")

    def edit_course_professor(self, course_name, professor_name):
        all_rows = self.read_file()
        final_row = []
        for row in all_rows:
            if course_name == row["course name"]:
                row["professor name"] = professor_name
            final_row.append(row)
            self.add_to_file(final_row, mode="w")

    def find_row_item(self, key_item, value_item):
        all_rows = self.read_file()
        for row in all_rows:
            if row[key_item] == value_item:
                return row
