print("hello world")
# x=5
# y=6
# z=x+y
# print(z)

# b=6+7j

# value=str(input("enter your name:"))
# print(value)
# print(b)



while True:
    try:
    
        name=input("Enter your name:").strip()
        
        Age= int(input("Enter your age:"))
        if Age<0:
            raise ValueError("Age should not be less than Zero(0)")
        break
    except ValueError as e:
        print(f"invalid input:{e}. Please try again")
        
        
        
def add_item():
    print("\nAdd New Item")
    # while True:
    #     try:
    #         name = input("Item name: ").strip()
    #         if not name:
    #             raise ValueError("Name cannot be empty")
                
    #         quantity = int(input("Quantity: "))
    #         if quantity < 0:
    #             raise ValueError("Quantity cannot be negative")
                
    #         price = float(input("Price: "))
    #         if price < 0:
    #             raise ValueError("Price cannot be negative")
                
    #         break
    #     except ValueError as e:
    #         print(f"Invalid input: {e}. Please try again.")
        
    # print("Hello")
    
    try:
            name = input("Item name: ").strip()
            if not name:
                raise ValueError("Name cannot be empty")
                
            quantity = int(input("Quantity: "))
            if quantity < 0:
                raise ValueError("Quantity cannot be negative")
                
            price = float(input("Price: "))
            if price < 0:
                raise ValueError("Price cannot be negative")
                
           
    except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
        
    print("Hello")
    
   
add_item()
    
    

