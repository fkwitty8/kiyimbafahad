import functionbase
import configurationfile

class Student:
    def __init__(self, studentid, courseid, student_name, email, contact ):
        self.studentid=studentid
        self.courseid=courseid 
        self.name=student_name
        self.email=email
        self.contact=contact
    
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


    def logout():
        
        return
    
    def register(student_name,email, contact, course_name):
        studentid=functionbase.generateid(type="student")
        courseid=functionbase.fetch_courseid(course_name)
        student={"id":studentid,"courseid":courseid,"name":student_name,"email":email,"cotact":contact}
        students=configurationfile.load_enity("student")
        students.append(student)
        configurationfile.save("student") 
        
        return
    
    
    def check_results():
        return
    
    def pay_tuition():
        return
    
    def send_Complaint_form():
        return
    

