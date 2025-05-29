import json
import os

INVENTORY_FILE="inventory.json"
CUSTOMER_FILE="customers.json"
ADMINISTRATOR_FILE="administrator.json"
LOGIN_STATUS=None
NOTAVAILALE="not_Availale"
ACCOUNT_FILE="useraccount.json"



def load_file(entity_Type):
    if entity_Type=="administrator":
        if os.path.exists(ADMINISTRATOR_FILE):
            with open(ADMINISTRATOR_FILE, "r") as administrator:
                 return json.load(administrator)
        return []
    elif entity_Type=="customer":
        
        if os.path.exists(CUSTOMER_FILE):
            with open(CUSTOMER_FILE,"r") as customer:
                return json.load(customer)
        return []
    elif entity_Type=="account":
        if os.path.exists(ACCOUNT_FILE):
            with open(ACCOUNT_FILE,"r") as account:
                return json.load(account)
        return []
        
    else:
        if os.path.exists(INVENTORY_FILE):
            with open(INVENTORY_FILE,"r") as inventory:
                return json.load(inventory)
        return []
    


def retrieve_Specific_Entity(entity_Type,entity_Name):
    
    retrieved_File=load_file(entity_Type)
   
    if entity_Type=="inventory":
        retrieved_Product=next( (product for product in retrieved_File if product.get("product_Name")==entity_Name), None)
        return retrieved_Product
            
    if entity_Type=="customer":
        retrieved_Customer=next( (customer for customer in retrieved_File if customer.get("username")==entity_Name), None)
        return retrieved_Customer
    
    
 
   
def persist_Entry(entity_Type,file):
    if entity_Type=="administrator":
        with open(ADMINISTRATOR_FILE, "w") as administrator:
            json.dump(file, administrator, indent=2)
        print("Saved changes successfully!")
        return
        
    if entity_Type=="customer":
        with open(CUSTOMER_FILE, "w") as customer:
            json.dump(file, customer, indent=2)
        print("Saved changes successfully!")
        return
    
    if entity_Type=="inventory":
        with open(INVENTORY_FILE, "w") as inventory:
            json.dump(file, inventory, indent=2)
        print("Saved changes successfully!")
        return
    
    if entity_Type=="account":
        with open(ACCOUNT_FILE, "w") as account:
            json.dump(file, account, indent=2)
        print("Saved changes successfully!")
        return
    
    
def user_ID(username):
    userID= next((user.get("user_ID") for user in load_file("customer") if user.get("username")==username),None)
    return userID


def account_No(userID):
    account_No= next((account.get("account_No") for account in load_file("account") if account.get("user_ID")==userID),None)
    return account_No

    


