import functionbase
import configurationfile

class Student:
    
    def __init__(self, studentid="", courseid="", student_name="", email="", contact="", course_name="", password="",account_id=""):
        self.studentid=studentid
        self.courseid=courseid 
        self.account_id=account_id
        self.name=student_name
        self.email=email
        self.contact=contact
        self.course_name=course_name
        self.password=password
        
    
    #TESTED
    #student= Student(email="hk",password="3")
    #student.login()
    def login(self):
        students_list=functionbase.load_entity("student")
        student=next((student for student in students_list if student.get("email")==self.email and student.get("password")==self.password),None)
        try:
            if not student:
                self.password=""
                self.email=""
                raise ValueError("invalid Username or pssword")
            print("login succesful!")
            return
        except ValueError as e:
            print(e)
            return
        
    def logout(self):
        print("logged out")
        return
    
    #TESTED
    #student= Student(email="hk",password="3")
    #student.register()
    def register(self ):
        
        #student_name,email, contact, course_name
        studentid=functionbase.generateid(entitytype="student")
        courseid=functionbase.generateid(entitytype="course")
        
        # student=Student(studentid,courseid,student_name,email,contact)
        self.studentid=studentid
        self.courseid=courseid
        
        
        student={"id":self.studentid,"courseid":self.courseid,"name":self.name,"email":self.email,"cotact":self.contact}
        
        students=configurationfile.load_enity("student")
        students.append(student)
        configurationfile.save("student",students)
        print("Registration successfull!")
        return
    
    
    def check_results(self):
        print("loding results")
        return
    
    def pay_tuition(self):
        print("Tuition paid")
        return
    
    def send_Complaint_form(self):
        print("sent")
        return
    
student= Student(email="hk",password="3")
student.login()
