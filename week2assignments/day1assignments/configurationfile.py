
#-----------------------loading user------------------
def load_enity(user_type):
    try:
        if type =="student":
            students=load_students()
            return students
        elif type=="lecturer":
            lecturers=load_lectures()
            return lecturers
        elif type=="course":
            courses=load_courses()
            return lecturers
        else:
            raise ValueError("inalid input")
    except ValueError as e:
        print(e)
        return

def load_students():
    with open("student.json", "r") as students:
        students=students.read()
    return students

def load_lectures():
    with open("lectures.json", "r") as lecturers:
        lecturers=lecturers.read()
    return lecturers

def load_courses():
    with open("courses.json", "r") as courses:
        courses=courses.read()
    return courses


#------------------------persisting enity to file-------------------
def save(type):
    try:
        if type=="student":
            save_student()
        elif type=="lecturer":
            save_lecturer
        else:
            raise ValueError("invalid input!")
    except ValueError as e:
        print(e)    

def save_student(students_file):
    with open("student.json","w") as students:
        students.dump(students_file, students)
        print("saved successfully!")
        return
                
def save_lecturer(lecurer_file):
    with open("lecurer.json","w") as lecturers:
        lecturers.dump(lecurer_file, lecturers)
        print("saved successfully!")
        return






    
        

    
