import configurationfile
        

#--------------------Registeration helper functions---------------------

def generateid(entitytype):#demonstrating polymormophism with abstraction
    print(entitytype)
    try:
        if entitytype=="student":
            studentid=generate_studentid()
            return studentid
        elif entitytype=="lecturer":
            lecturerid=generate_lecturerid()
            return lecturerid
        elif entitytype=="course":
            courseid=generate_courseid()
            return courseid
        else:
            raise ValueError("invalid input")
        
    except ValueError as e:
        print(e)
        return       

def generate_studentid():
    students=configurationfile.load_enity("student")
    print(students)
    studentid=max([int(student["id"] )for student in students],default=0)
    return studentid

def generate_lecturerid():
    lecturers=configurationfile.load_enity("lecturer")
    lecturerid=max([lecturer.get("lecturerid") for lecturer in lecturers],default=0)+1
    return lecturerid

def generate_courseid():
    courses=configurationfile.load_enity("course")
    courseid=max([course.get("courseid") for course in courses],default=0)+1
    return courseid



#----------------fetching ids for referencing---------------
def fetch_courseid(course_name):
    courses=configurationfile.load_enity("course")
    courseid=next((course.get("id") for course in courses if course.get("course_name"==course_name)),None)
    return courseid


#------------------main screen menu---------------
def start_screen(): 
    print(f"\n\n--------\033[92mFMAKERERE UNIVERSITY\033[0m--------")
    user_input=input("\n    view courses offered\n    login\n    register\n(viewcourses/login/register/close)\n>>>").lower().strip()
    return user_input