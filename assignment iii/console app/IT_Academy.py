import csv
import os

import prettytable

class Academy:

    def __init__(self,courses_file, student_file):
        self.courses = courses_file
        self.students = student_file

    def display_courses_info(self):
        course_table = self.display_table(self.courses)
        print(course_table)
     
    
    def register_student(self):
        info = ['u_id','fname','lname','course','gender','adress','email','phone','paid','due']
        student_data = []
        last_id = int(self.id_generate())
        for field in info:
            if field == 'u_id':
                value = last_id + 1
                value = str(value) # convert to string
            else:
                value = input("Enter {}: ".format(field))
            student_data.append(value)
        
        with open('dummy.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerows([student_data])
    

    def id_generate(self):
        with open('dummy.csv', 'r') as f:
            reader = csv.DictReader(f)
            temp_li = []
            for row in reader:
                temp_li.append(row)
            last_id = temp_li[-1]['u_id']
            return last_id
    

    def student_list(self):
        student_table = self.display_table(self.students)
        print(student_table)


    def delete_student(self,id_no):
        with open('dummy.csv', 'r') as readFile, open('dummy_new.csv','w') as writeFile:
            reader = csv.DictReader(readFile)
            fieldnames =['u_id','fname','lname','course','gender','adress','email','phone','paid','due']
            writer = csv.DictWriter(writeFile,fieldnames=fieldnames)
            writer.writeheader()
            for row in reader:
                if dict(row)['u_id'] == id_no:
                    continue
                writer.writerow(dict(row))
        os.remove('dummy.csv')
        os.rename('dummy_new.csv','dummy.csv')

    
    def update_student_info(self, id_no):
        with open('dummy.csv', 'r') as readFile, open('dummy_new.csv','w') as writeFile:
            reader = csv.DictReader(readFile)
            fieldnames =['u_id','fname','lname','course','gender','adress','email','phone','paid','due']
            student_data = {}
            writer = csv.DictWriter(writeFile,fieldnames=fieldnames)
            writer.writeheader()
            for row in reader:
                if dict(row)['u_id'] == id_no:
                    for item in fieldnames:
                        if item == "u_id":
                            student_data["u_id"] = id_no
                        else:
                            student_data[item] = input("Enter updated {}".format(item))
                    writer.writerow(dict(student_data))
                else:
                    writer.writerow(dict(row))
        os.remove('dummy.csv')
        os.rename('dummy_new.csv','dummy.csv')


    def course_refund(self):
        student_id = input("u_id of student that completed the course")
        self.delete_student(student_id)
        print("You will receive refund of Rs 3000 in cheque ")

    

    def display_table(self, filename):
        table = None
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if table is None:
                    table = prettytable.PrettyTable(row)
                else:
                    table.add_row(row)
        return table
            



class Menu:

    def __init__(self, academy:Academy):
        self.academy = academy
    

    def main_menu(self):
        while True:
            choice = input(
                '''
                1. Query Available Courses
                2. Student Information
                3. Student Registration
                4. Delete Record
                5. Update Student Record
                6. Refund after completion of course
                7. Exit
                '''
            )
            if choice not in ['1','2','3','4','5','6','7']:
                print('Enter the correct choices from 1 to')
            else:
                return choice
    

    def previous_page(self):
        while True:
            return input("Return to main menu: ")[0].lower() != 'y'

    def run(self):
        while True:
            user_choice = self.main_menu()
            if user_choice == "1":
                while True:
                    user_choice = self.academy.display_courses_info()
                    if not self.previous_page():
                        break
            elif user_choice=="2":
                while True:
                    print("Register in course ")
                    self.academy.student_list()
                    if not self.previous_page():
                        break
            elif user_choice=="3":
                while True:
                    print("Register new student")
                    self.academy.register_student()
                    if not  self.previous_page():
                        break
            elif user_choice == '4':
                while True:
                    print("Provide the student info to delete")
                    self.academy.delete_student(input("Enter the id of student: "))
                    if not self.previous_page():
                        break
            
            elif user_choice == '5':
                while True:
                    print("Provide the student info to update")
                    self.academy.update_student_info(input("Enter the id of student: "))
                    if not self.previous_page():
                        break

            elif user_choice == '6':
                while True:
                    print("Reund for course completion")
                    self.academy.courses()
                    if not self.previous_page():
                        break
            
            elif user_choice == '7':
                break




def main():
    print(
        '''

        ==================== Welcome to IT Academy ====================

        '''
    )
    academy = Academy('courses.csv','dummy.csv')
    menu = Menu(academy)
    menu.run()


if __name__ == "__main__":
    main()

            