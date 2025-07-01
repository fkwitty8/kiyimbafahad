"""input two numbers, divide them, use infinite loop untill if error occurs"""

def division(first_number,second_number):#divides any two numbers
    try:
        if not check_ifintegers(first_number, second_number):
            raise ValueError("one of/both of the characters entered is/are not number(s) ")
        first_number=int(first_number)
        second_number=int(second_number)
        
        if second_number==0:#checking if second factor is Zero
            raise ValueError("cant Divide by Zero!")  
        return first_number/second_number
    except ValueError as e:
        print(e)
        
def check_ifintegers(first_number,second_number):#checks for integers
    if isinstance(first_number,int) and isinstance(second_number,int):
        return True
    return False      
    

def main():
    control=""
    while True:
        if control=="exit":
            break
        delimeter=","
        user_input_array=input(f"\nEnter two number whose quotient is to be found[a,b]:\n>>> ").strip().split(delimeter)
        try:
            if len(user_input_array)!=2:#validating number user inputs
                raise ValueError("Can't operate on one number or more than two factors!")
    
            first_number=(user_input_array[0])
            second_number=(user_input_array[1])
            quotient=division(first_number, second_number)
            
            print(f"The quotient of {first_number} and {second_number} is {quotient}")  
            control=input("\nPress any Key to continue or enter [exit] to close:\n>>>")
        except ValueError as e:
            print(e)
        
        
    return

main()