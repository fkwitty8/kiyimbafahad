import functionbase
import configurationfile

class Student:
    
    def __init__(self, studentid="", courseid="", student_name="", email="", contact="", course_name="" ):
        self.studentid=studentid
        self.courseid=courseid 
        self.name=student_name
        self.email=email
        self.contact=contact
        self.course_name=course_name
    
    def login(email, password):
        
        students_list=configurationfile.load_user("student")
        student=next((student for student in students_list if student.get("email")==email and student.get("password"==password)),None)
        try:
            if not student:
                raise ValueError("invalid Username or pssword")
            print("login succesful!")
            return
        except ValueError as e:
            print(e)
            return


    def logout(self):
        print("H")
        return
    
    def register(self ):
        
        #student_name,email, contact, course_name
        studentid=functionbase.generateid(entitytype="student")
        courseid=functionbase.fetch_courseid(self.course_name)
        
        # student=Student(studentid,courseid,student_name,email,contact)
        self.studentid=studentid
        self.courseid=courseid
        
        
        student={"id":self.studentid,"courseid":self.courseid,"name":self.name,"email":self.email,"cotact":self.contact}
        
        students=configurationfile.load_enity("student")
        students.append(student)
        configurationfile.save("student",students)
        
        return
    
    
    def check_results(self):
        print("H")
        return
    
    def pay_tuition(self):
        print("H")
        return
    
    def send_Complaint_form(self):
        print("H")
        return
    

student= Student(student_name="bk",email="bk",contact=13)
student.register()