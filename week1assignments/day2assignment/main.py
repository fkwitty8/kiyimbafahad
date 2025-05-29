
import sharedfunctionalities
import configurationfile
import admininterface
import customerinterface

# """INVENTORY MANAGEMENT SYSTEM"""
# """BASIC METHODS"""

# """Administrattors side"""
# #adding product(s)
# #deleting product(s)
# #updating product(s) 
#view customers--(done)
#serch_agivenCustomer_byName--(done)
#suspend user




# """Customers side"""
# register


# """shared methods"""
# #login--admin(done),customer(done)
# #logout--admin(done),customer()
# #register
# #serch product--admin(done),customer()
# #viewproducts--admin(done),customer()
#close--admin(done),customer()
#deposit
#check_balance
#buy
#byproduct
#transferFunds
#create account




def main():
    #returned_value messges
    """
    loginok
    logout>continue
    close>break
    """
    while True:

        user_input= start_screen()
        returned_value, type=menu_management(user_input)
        
        
        if returned_value=="loginok":#login screen
            returned_value=entity_login_screen(type)
            if returned_value=="logout":
                continue
            elif returned_value=="close":
                break
        
  
  
def start_screen(): 
    print(f"\n\n--------\033[92mFAHAD SUPERMARKET INVENTORY\033[0m--------")
    user_input=input("\n    1. view Available products\n    2. login\n    3. register\n(viewproduct/login/register/close)\n>>>").lower().strip()
    return user_input


def entity_login_screen(entity_type):
    if entity_type=="administrator":
        admininterface.admin_interface()
    else:
        customerinterface.customer_interface
    return
        
def menu_management(user_input):
    if user_input=="viewproduct":
        while True:
            user_input=input("search product name or view all products\n(byname/allproducts/exit)\n>>>").lower().strip()
            if user_input.strip()=="byname":
                user_input=input("Enter the products name:\n>>>").strip().lower()
                sharedfunctionalities.search_Entityby_Name(user_input)

            if user_input=="allproducts":
                sharedfunctionalities.display_Entity(entity_Type="inventory", single_Entity=False)
                
            if user_input=="exit":
                break
            
    elif user_input=="login":
        while True:
            user_input=input("Enter exit to quit or press any key to proceed.(exit/):\n>>>").lower().strip()
            if user_input=="exit":
                return
            user_name=input("    Enter your username: ")
            password=int(input("    Enter your password: "))
            type=input("    Enter role(customer/administrator): ")
            
            login_state=sharedfunctionalities.login(user_name,password,type)
            return login_state,type
        
    elif user_input=="register":
        while True:
            user_input=input("Enter exit to quit or press any key to proceed.(exit/):\n>>>").lower().strip()
            if user_input=="exit":
                return
            user_name=input("   Enter your username: ")
            password=int(input("   Enter your password: "))
            type=input("   Enter role(customer/administrator): ")
            
            
            
            login_state=sharedfunctionalities.login(user_name,password,type)
            return login_state,type
        
    elif user_input=="close":
            return user_input 
    
    else:
         print("invalid input!")
         
           
        
    return


    
        
       
main()


    




