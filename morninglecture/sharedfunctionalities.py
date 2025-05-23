import configurationfile
import json


#TETSTED
def login(username, password, entity_Type): 
    
    #cheking and retrieving relevant entity jsonfile
    State=None
    retrieved_File=configurationfile.load_file(entity_Type)
    print(retrieved_File)
    try:
        retrieved_user=next((user for user in retrieved_File if user.get("username")==username and user.get("password")==password),None)
        print(retrieved_user)
        if  not retrieved_user :
            raise ValueError("invalid username or password!")
        return 
    except ValueError as e:
        print(e)
        
    State="Failed"
    return State


#TESTED
def register(entity_Type):
    retrieved_File=configurationfile.load_file(entity_Type)
    print(retrieved_File)
    username=input("Enter your user name:\n>>>").strip()
    password=input ("enter your password:>>>\n").strip()
    
    retrieved_File.append({"username":username, "password":password})
    save_Entity(entity_Type, retrieved_File)
    return
    
   
#TETSED    
def save_Entity(entity_Type, file):
    configurationfile.persist_Entry(entity_Type,file)


#TESTED
#search_Entityby_Name("jk","customer" ) 
def search_Entityby_Name(entity_Name, entity_Type="inventory", Who="administrator"):
    retrieved_serched_Item=configurationfile.retrieve_Specific_Entity(entity_Type,entity_Name)
  
    
    try:
        if not retrieved_serched_Item:
            raise ValueError("No product found!")
        display_Entity(entity_Type,retrieved_serched_Item)
        return
    except ValueError as  e:
        print(e)
        
        
#TESTED
#display_Entity(entity_Type="customer", single_Entity=False)
def display_Entity(entity_Type=None, entityto_Display=None, Who="administrator", single_Entity=True):
    
    # """ADMINISTRATOR DISPLAY"""
    if Who=="administrator":
        #if display for a singleitem
        if single_Entity:
            #customer search
            if entity_Type=="customer":
                print("\n {}".format("|      UserName    |"))
                print(" -"*10)
                print(f"\n|          {entityto_Display.get("username")}       |")
                return
            #invntory search
            if entity_Type=="inventory":
                print("\n {:<1} {:<1} {:<24} {:<10} {:<1} {:<1}".format("| ProductName |","Price |","AvilableQuantity |", "state |","|        StockLevel      |", "Initial_Stock |"))
                print(" -"*52)
                print("\n{:<16} {:<12} {:<16} {:<18} {:<26} {:<1}".format(entityto_Display.get("product_Name"), entityto_Display.get("price"), entityto_Display.get("availale_Quantity"), entityto_Display.get("state"),entityto_Display.get("stock_Level"),entityto_Display.get("initial-stock")))
                return
        
        
        #if display for multiple items
        retrieved_Items=configurationfile.load_file(entity_Type)
        
        
        #if customer search
        if entity_Type=="customer":
            
            print("\n {}".format("|      UserName    |"))
            print(" -"*10)
            for customer in retrieved_Items:
                print(f"\n|          {customer.get("username")}       |")
            return
        
        #if product search
        print(retrieved_Items)
        print("\n {:<1} {:<1} {:<24} {:<10} {:<1} {:<1}".format("| ProductName |","Price |","AvilableQuantity|", "state ","|        StockLevel      |", "Initial_Stock |"))
        print(" -"*52)
        for product in retrieved_Items:
            print("\n{:<16} {:<12} {:<16} {:<18} {:<26} {:<1}".format(product.get("product_Name"), product.get("price"), product.get("availale_Quantity"),product.get("state"),product.get("stock_Level"),product.get("initial-stock")))
        return
    
        
    # """CUSTOMER DISPLAY"""    
    #if display for a singleitem
    if single_Entity:
        #product search
        print("\n {:<1} {:<1} {:<20} {:<10}".format("ProductName","Price","AvilableQuantity", "state"))
        print(" -"*26)
        print("\n{:<16} {:<14} {:<12} {:1} ".format(entityto_Display.get("product_Name"), entityto_Display.get("price"), entityto_Display.get("availale_Quantity"), entityto_Display.get("state")))
        return        
       
    #multiple products
    retrieved_Items=configurationfile.load_file(entity_Type)
    print("\n {:<1} {:<1} {:<20} {:<10}".format("|  ProductName |","Price |","AvilableQuantity|", "state |",))
    print(" -"*26)
    for product in retrieved_Items :     
        print("\n{:<16} {:<14} {:<12} {:1} ".format(product.get("product_Name"), product.get("price"), product.get("availale_Quantity"), product.get("state")))
    return        
    

#TESTED
#purchase_item([{"product_Name":"Burger", "product_Quantity":3}],1)
def purchase_item(product_cart_list, account_No, ):
    print("Hello")
    total_Cost=0
    balance=0
    
    for cart in product_cart_list:
        product_Name=cart.get("product_Name") 
        product_Quantity=cart.get("product_Quantity")   
    
        balance=next((account.get("balance") for account in configurationfile.load_file("account") if account.get("account_Number")==account_No ),None)
        product=next((product for product in configurationfile.load_file("inventory") if product.get("product_Name")==product_Name ),None)
        print(product)

        try:
            if product_Quantity>product.get("available_Quantity"):
                raise ValueError("purchased more than avilable Quantity!")
        
            total_Cost+=(product.get("price")*product_Quantity)
        except ValueError as e:
            print(f"{product_Name} {e}")
        
        
    try:
        print(total_Cost)
        print(balance)
        
        if total_Cost>balance:
            raise ValueError("insufficient Funds!") 
        update_stock(product_cart_list)
        debt_account(total_Cost,account_No)
    
    except ValueError as e:
        print(e)
        return "FAILED"



    
    
"""USER ACCOUNT MANAGEMENT"""

def deposit(amount, account_number):
    account= next((account for account in configurationfile.load_file("account") if account.get("account_Number")==account_number))
    account["balance"]+=amount
    print(f"deposit succesful! \naccount balance is {account["balance"]} ")
    return 

#TESTED
def debt_account(total_Cost, account_No):
    returned_Accounts=configurationfile.load_file("account")
    account=next((account for account in returned_Accounts if account.get("account_Number")==account_No ),None)
    print(total_Cost)
    print(account)
    account["balance"]-=total_Cost
    save_Entity("account", returned_Accounts)
    return


    
"""INVENTORY MANAGEMENT"""
#TESTED but not copmlete

def update_stock(product_cart_list):
    returned_Stock=configurationfile.load_file("product")
    for cart in product_cart_list:
        product_Name=cart.get("product_Name") 
        product_Quantity=cart.get("product_Quantity") 
        product=next((product for product in returned_Stock  if product.get("product_Name")==product_Name ),None)#retrieving product matching the name
        product["available_Quantity"]-=product_Quantity#updaing product quantity
        #updating product state
         
        index=next((index for index, product in enumerate(returned_Stock ) if product.get("product_Name")==product_Name ),None) #getting products index inlist       
        returned_Stock[index]=product
        save_Entity("inventory",returned_Stock)
         
    return 


def update_derived_productfields(product):
    
    return
        
    
