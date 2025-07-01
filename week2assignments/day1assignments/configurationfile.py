import json
import os

#-----------------Constants----------------------
STUDENTS_FILE="student.json"
LECTURES_FILE="lectures.json"
COURSES_FILE="courses.json"


#-----------------------loading user------------------
def load_enity(user_type):
    try:
        if user_type =="student":
            students=load_students()
            return students
        elif type=="lecturer":
            lecturers=load_lectures()
            return lecturers
        elif user_type=="course":
            courses=load_courses()
            return courses
        else:
            raise ValueError("invalid input")
    except ValueError as e:
        print(e)
        

def load_students():
    if os.path.exists(STUDENTS_FILE):
        with open(STUDENTS_FILE, "r") as students:
            return json.load(students)
    
def load_lectures():
    if os.path.exists(LECTURES_FILE):
        with open(LECTURES_FILE, "r") as lecturers:
            return json.load(lecturers)
    
def load_courses():
    if os.path.exists(COURSES_FILE):
        with open(COURSES_FILE, "r") as courses:
            return json.load(courses)


#------------------------persisting enity to file-------------------
def save(type,file):
    try:
        if type=="student":
            save_student(file)
        elif type=="lecturer":
            save_lecturer(file)
        else:
            raise ValueError("invalid input!")
    except ValueError as e:
        print(e)    

def save_student(students_file):
    with open("student.json","w") as students:
        json.dump(students_file, students, indent=1)
        print("saved successfully!")
        return
                
def save_lecturer(lecurer_file):
    with open("lecurer.json","w") as lecturers:
        json.dump(lecurer_file, lecturers,indent=1)
        print("saved successfully!")
        return






    
        

    
