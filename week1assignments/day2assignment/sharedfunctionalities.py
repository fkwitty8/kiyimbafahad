import configurationfile
import json
import random


#TETSTED
#login("admin",12,"administrator") 
def login(username, password, entity_Type): 
    
    #cheking and retrieving relevant entity jsonfile
    State="loginfailed"
    retrieved_File=configurationfile.load_file(entity_Type)
    try:
        retrieved_user=next((user for user in retrieved_File if user.get("username")==username and user.get("password")==password),None)
        if  not retrieved_user :
            raise ValueError("\ninvalid username or password!")
        print("\nlogin successfull")
        State="loginok"
        return State
    except ValueError as e:
        print(e)


#TESTED
def register(entity_Type):
    retrieved_File=configurationfile.load_file(entity_Type)
    username=input("Enter your user name:\n>>>").strip()
    password=input ("enter your password:>>>\n").strip()
    
    retrieved_File.append({"username":username, "password":password})
    save_Entity(entity_Type, retrieved_File)
    return
    
   
#TETSED    
def save_Entity(entity_Type, file):
    configurationfile.persist_Entry(entity_Type,file)


#TESTED
#search_Entityby_Name("jk","customer" ) /search_Entityby_Name("jk","customer" ,Who="administrator") 
def search_Entityby_Name(entity_Name, entity_Type="inventory", Who="customer"):
    retrieved_serched_Item=configurationfile.retrieve_Specific_Entity(entity_Type,entity_Name)
        
    try:
        if not retrieved_serched_Item:
            raise ValueError("No product found!")
        display_Entity(entity_Type=entity_Type,entityto_Display=retrieved_serched_Item,Who=Who)
        return
    except ValueError as  e:
        print(e)
        
        
#TESTED
#display_Entity(entity_Type="customer", single_Entity=False)/search_Entityby_Name("jk","customer", Who="administrator") 
def display_Entity(entity_Type=None, entityto_Display=None, Who="customer", single_Entity=True):#used to search a single or many product by either a customer or an adminstraor
    
    # """ADMINISTRATOR DISPLAY"""
    if Who=="administrator":
        #if display for a singleitem
        if single_Entity:
            #sile customer search
            if entity_Type=="customer":
                print("\n {}".format("|      UserName    |"))
                print(" -"*10)
                print(f"\n|          {entityto_Display.get("username")}       |")
                return
            #single invntory search
            if entity_Type=="inventory":
                
                print("\n {:<1} {:<1} {:<24} {:<10} {:<1} {:<1}".format("| ProductName |","Price |","AvilableQuantity |", "state |","|        StockLevel      |", "Initial_Stock |"))
                print(" -"*52)
                print("\n{:<16} {:<12} {:<16} {:<18} {:<26} {:<1}".format(entityto_Display.get("product_Name"), entityto_Display.get("price"), entityto_Display.get("available_Quantity"), entityto_Display.get("state"),entityto_Display.get("stock_level"),entityto_Display.get("initial_stock")))
                return
        
        
        #if display for multiple items
        retrieved_Items=configurationfile.load_file(entity_Type)
                
        #multiple customer search
        if entity_Type=="customer":
            
            print("\n {}".format("|      UserName    |"))
            print(" -"*10)
            for customer in retrieved_Items:
                print(f"\n|          {customer.get("username")}       |")
            return
        
        #multiple products search
        print("\n {:<1} {:<1} {:<24} {:<10} {:<1} {:<1}".format("| ProductName |","Price |","AvilableQuantity|", "state ","|        StockLevel      |", "Initial_Stock |"))
        print(" -"*52)
        for product in retrieved_Items:
            print("\n{:<16} {:<12} {:<16} {:<18} {:<26} {:<1}".format(product.get("product_Name"), product.get("price"), product.get("available_Quantity"),product.get("state"),product.get("stock_level"),product.get("initial_stock")))
        return
    
        
    # """CUSTOMER DISPLAY"""    
    #if display for a singleitem
    if single_Entity:
        #product search
        print("\n {:<1} {:<1} {:<20} {:<10}".format("|  ProductName |","Price |","AvilableQuantity|", "state    |"))
        print(" -"*29)
        print("\n  {: <16} {:<12} {:<12} {:<1} ".format(entityto_Display.get("product_Name"), entityto_Display.get("price"), entityto_Display.get("available_Quantity"), entityto_Display.get("state")))
        return        
       
    #multiple products
    retrieved_Items=configurationfile.load_file(entity_Type)
    print("\n {:<1} {:<1} {:<20} {:<10}".format("|  ProductName |","Price |","AvilableQuantity|", "state    |"))
    print(" -"*29)
    for product in retrieved_Items :     
        print("\n  {:<16} {:<12} {:<12} {:<1} ".format(product.get("product_Name"), product.get("price"), product.get("available_Quantity"), product.get("state")))
    return        
    

#TESTED
#purchase_item([{"product_Name":"Burger", "product_Quantity":3}],1)
def purchase_item(product_cart_list, user_name):
    total_Cost=0

    
    user_id=configurationfile.user_ID(user_name)#retrieveing user ID

    for cart in product_cart_list:
        product_Name=cart.get("product_Name") 
        product_Quantity=cart.get("product_Quantity")   
        try:
            account=next((account for account in configurationfile.load_file("account") if account.get("user_id")==user_id ),None)
            if account is None:
                raise ValueError("You have no account yet")
            product=next((product for product in configurationfile.load_file("inventory") if product.get("product_Name")==product_Name ),None)
    
            
            if product_Quantity>product.get("available_Quantity"):
                raise ValueError("purchased more than avilable Quantity!")
            if product.get("state")=="out of stock":
                raise ValueError("purchased is out of Stock")
        
            total_Cost+=(product.get("price")*product_Quantity)
        except ValueError as e:
            print(f"{product_Name} {e}")
       
        
        update_stock(product_cart_list)
        debt_account(total_Cost,user_name)
    

        return "FAILED"


#TESTED
#validate_product_list([{"product_Name": "dud","available_Quantity": 2,},{"product_Name": "dude","available_Quantity": 700,}])
#validates names of products on buying by a customer  before further processing
def validate_product_list(list, type="inventory"):    
    vaidated_lists=[]
            
    for cart in list:
            
        validated_list=[entity_list for entity_list in configurationfile.load_file(type) if entity_list.get("product_Name")==cart]
        try:
            if not validated_list:
                raise ValueError("not system!")
            vaidated_lists.append(cart)
        except ValueError as e:
            print(f" {cart} {e}")
     
    return vaidated_lists            
    
    
            

    
    
"""USER ACCOUNT MANAGEMENT"""
#TESTED
#deposit(300,1)
def deposit(amount, account_No):
    returned_accounts=configurationfile.load_file("account")
    account= next((account for account in configurationfile.load_file("account") if account.get("account_Number")==account_No))
    try:
        if account is None: 
            raise ValueError("Incorrect account Number")
    except ValueError as e:
        print(e)
        
    account["balance"]+=amount
    
    index=next((index for index, account in enumerate(returned_accounts ) if account.get("account_Number")==account_No ),None) #getting account index inlist       
    returned_accounts[index]=account
    save_Entity("account", returned_accounts)
    
    print(f"deposit succesful! \naccount balance is now {account["balance"]} ")
    return 


#TESTED
def debt_account(total_Cost, user_name):
    user_id=configurationfile.user_ID(user_name)#retrieveing user ID
    returned_accounts=configurationfile.load_file("account")
    accounts=[account for account in returned_accounts if account.get("user_id")==user_id]
    print(account)
    account_no=input("\n   Choose which account(Enter the account Number)\n")
    account= next((account for account in accounts if account.get("account_Number")==account_no))
    try:
        
        if not account:
            raise ValueError ("invalid account number")
        if account.get("state")=="fozen":
            raise ValueError("This account as frozen")
        
        if total_Cost>account.get("balance"):
            raise ValueError("insufficient Funds!") 
        account["balance"]-=total_Cost

        index=next((index for index, account in enumerate(returned_accounts ) if account.get("user_id")==user_id ),None) #getting account index inlist       
        returned_accounts[index]=account
        save_Entity("account", returned_accounts)
        return
        
    except ValueError as e:
        print(e)
    
    


    
"""INVENTORY MANAGEMENT"""
#TESTED
#update_stock([{"product_Name":"pizza","product_Quantity":300},{"product_Name":"burger","product_Quantity":200}])
def update_stock(product_list,acivity="decrement"):
    returned_Stock=configurationfile.load_file("product")
    
    for cart in product_list:
        product_Name=cart.get("product_Name")
        product_Quantity=cart.get("product_Quantity") 
        product=next((product for product in returned_Stock  if product.get("product_Name")==product_Name ),None)#retrieving product matching the name

        
        if acivity=="decrement":#selling
            product["available_Quantity"]-=product_Quantity#updaing product quantity
            product=update_derived_productfields(product)
            
        else :#increment/addind product
            #checking whether product already exits          
            if not product:
                returned_Stock.append(cart)
                product=cart
            else:
                product["available_Quantity"]+=product_Quantity#updaing product quantity
                
            
        #updating product state and stocklevel
        product=update_derived_productfields(product)
               
        index=next((index for index, product in enumerate(returned_Stock ) if product.get("product_Name")==product_Name ),None) #getting products index inlist       
        returned_Stock[index]=product
        
        
        save_Entity("inventory",returned_Stock)
         
    return 


def update_derived_productfields(product):#derives state, stocklevel
    #for state if its below if>=70%"instock",>=30 "understock",<30 out of stock
    if (product["available_Quantity"]/product["initial_stock"])*100>=70:
        product["state"]="instock"
        product["stock_level"]=(product["available_Quantity"]/product["initial_stock"])*100   
    elif (product["available_Quantity"]/product["initial_stock"])*100>=30: 
        product["state"]="understock"
        product["stock_level"]=(product["available_Quantity"]/product["initial_stock"])*100   
    else:
        product["state"]= "out of stock"
        product["stock_level"]=(product["available_Quantity"]/product["initial_stock"])*100   
    
    return product


#TESTED
# check_account_balance(1,2)
def check_account_balance(account_no,pincode):
    returned_accounts=configurationfile.load_file("account")
    account=next((account for account in returned_accounts if account.get("account_Number")==account_no ),None)
    try:
        if account is None: 
            raise ValueError("Incorrect account Number")
    
        if account["pincode"]!=pincode:
            raise ValueError("Incorrect pincode")
        
        print(f"your account balance is {account["balance"]}")
        
    except ValueError as e:
        print(e)
    
    return 

#TESTED
#add_product(products)
def add_product(products_list):
    update_stock(products_list, acivity="increment")
    return
             
 
#TESTED
#delete_product("dude")
def delete_product(product_names):
    retrieved_proucts=configurationfile.load_file("product")
    for product_name  in product_names:
        product=next((product for product in retrieved_proucts if product.get("product_Name")==product_name),None)
        index=next((index for index, product in enumerate(retrieved_proucts ) if product.get("product_Name")==product_name ),None) #getting account index inlist       

        try:
            if not product:
                raise ValueError(f"{product_name} does not exist!")
            retrieved_proucts.pop(index)
            print(f"deleted  product {product_name} successfull!")
            save_Entity("inventory",retrieved_proucts)
            return
        except ValueError as e:
            print(e) 
        finally:
            product_names=[] 
        
         
#TESTED
#suspend_account("fK")
def suspend_account(user_name):
    retrieved_user=configurationfile.load_file("customer")
    user=next((user for user in retrieved_user if user.get("username")==user_name),None)
    try:
        if not user:
            raise ValueError(f"user {user_name} does not exist! ")
        retrieved_user=configurationfile.load_file("account")
        #getting user id
        user_id=configurationfile.user_ID(user_name)
        retrieved_accounts=configurationfile.load_file("account")
        accounts=[account for account in retrieved_accounts if account.get("user_id")==user_id]
        #checking if user has an account
        if not accounts:
            raise ValueError(f"user {user_name} has no account")
        print(f"user{user_name} has the following accounts:")
        while True:
            for account in accounts:#listing account numbers to user
                print(f"{account.get("account_Number")}\n")
        
            account_numbers=[]
            user_input=int(input("\nEnter account number(s) to suspend or enter [next] to proceed:\n>>>").lower().strip())
            while True:
                if user_input=="next":
                    user_input=None
                    break
                account_numbers.append(user_input)
                user_input=input(">>>").lower().strip()
             
            validated_list =[]  
            for account_number in account_numbers:
                for account in accounts:
                    if account_number==account.get("account_Number"):
                        validated_list.append(account_number)
                        
           
            #checking if account if already frozen
            
            for account_no in validated_list:
                account=next((account for account in retrieved_accounts if account.get("user_id")==user_id),None)
                
                if account.get("state")=="frozen":
                    raise ValueError(f"Account to user {user_name} is alreasy frozen!")
                account["state"]="frozen"
                index=next((index for index, account in enumerate(retrieved_accounts ) if account.get("user_id")==user_id ),None) #getting account index inlist       
                retrieved_accounts[index]=account
                
            print(f"accout(s) to user {user_name} has been frozen successfully!")
            save_Entity("account", retrieved_accounts) 
            #sending notification to user 
            return  
    except ValueError as e:
            print(e)  
            
            
#TESTED
#create_account("dk")
def create_account(user_name):
    retrieved_accounts=configurationfile.load_file("account")
    #check if user has accounts not more than 3
    user_id=configurationfile.user_ID(user_name)
    
    accounts=[account for account in retrieved_accounts if account.get("user_id")==user_id]
    try:
        if len(accounts)>=3:
            raise ValueError("can't exceed maximum number of account ")
        #generating account number
        account_numbers=[account.get("account_Number") for account in accounts]
        account_number=0
        while True:
            number=random.randint(0,999999999999999999999999999999)
            if number not in account_numbers :
                account_number=number
                break
         
        
        while True:   
            pincode1=input("\n   Enter your pincode or [exist] to quit\n")
            pincode2=input("\n   Re-Enter your pincode\n")
            if pincode1=="exit":
                print("account set-up declined!")
                break
            if pincode1!=pincode2:
                raise ValueError("pincodes dont match!")
            
            new_account={"user_id": user_id,"account_Number": account_number,"pincode": pincode2,"balance": 0,"state":"active"}
            retrieved_accounts.append(new_account)
            save_Entity("account",retrieved_accounts)
            print("\n account created successfully!")
            break
        
        return
                
    except ValueError as e:
        print(e)
        

