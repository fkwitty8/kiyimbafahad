"""
# UNIVERSITY MANAGEMENT SYSTEM"""
# """BASIC METHODS"""

# """lecturers"""
# login
# logout
# #upload marks
# #upload Notes
    #>>>generalised to upload file
# View retaking students by year
# View redoing students By year
# #views studients offering their course unit



# """Student"""
#>>>categories(ineternation/ local students)
# login
# logout
# register
# enrol to a course
# download permit
# download Notes
    #>>>download file
# check results
# send a compalint form to HOD
# pay tution


# """ course"""
#enrol



# """shared methods"""




def main():
    start_screen()

def start_screen(): 
    print(f"\n\n--------\033[92mFMAKERERE UNIVERSITY\033[0m--------")
    user_input=input("\n    view courses offered\n    login\n    register\n(viewcourses/login/register/close)\n>>>").lower().strip()
    return user_input.strip()

