
import sharedfunctionalities
import configurationfile

# """INVENTORY MANAGEMENT SYSTEM"""
# """BASIC METHODS"""

# """Administrattors side"""
# #adding a product
# #deleting a product
# #searching a product
# #updating a product 
# #login
# #logout
# #viewproduct


# """Customers side"""
# #login
# #logout
# #view product
# #byproduct
# #serch for product
# #register

# """shared methods"""
# #login
# #logout
# #register
# #serch product
# #viewproduct




def main():
    print(f"FAHAD SUPERMARKET INVENTORY")
    
    """REGISTER"""
    #configurationfile.CUSTOMER_FILE.append({"username":"fk", "password":123})
    
    
    """LOGIN"""
    print("Hello")
    while True:
        print(f"login as: administrator or customer")
        entity_Type=input(">>>: ").strip()
        entity_Type.lower()
    
        username=input("Enter your Username:\n>>>").strip()
        password=input("Enter your Password:\n>>>").strip()
        print(username)
        print(password)
    
        login_Return=sharedfunctionalities.login(username, password, entity_Type)
        
        if login_Return=="Failed":
            continue
        configurationfile.LOGIN_STATUS="loggedin"
        print("logged successfully!")
        break
    
main()
    




