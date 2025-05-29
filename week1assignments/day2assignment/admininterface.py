
import sharedfunctionalities
import configurationfile


def admin_interface(entity_type="administrator"):
    while True:
            
            print("\n\n--------ADMINISTRATOR PANNEL--------")
            user_input=input("\n    1. logout\n    2. manage product(s)\n    3. manage customer(s)\n    4. maketransactions(s)\n(logout/products/customers/ transactions/close)\n>>>").lower().strip()
            if user_input=="logout":
                print("Your are now logged out!")
                return user_input
            if user_input=="close":
                return user_input
            if user_input=="products":
                while True:
                    print("\n\n--------product management pannel--------")
                    user_input=input("\n    1. search product by name\n    2. view poducts\n    3. add product(s)\n    4. delete product(s)\n(searchproduct/allproducts/delete/add/exit)\n>>>").lower().strip() 
                    if user_input=="exit":
                        break
                    if user_input=="searchproduct":
                        user_input=input("\nEnter product name:\n>>>").lower().strip()
                        sharedfunctionalities.search_Entityby_Name(user_input, Who=entity_type)
                        continue
                    if user_input=="allproducts":
                        sharedfunctionalities.display_Entity( entity_Type="inventory",single_Entity=False ,Who=entity_type)
                        continue
                    if user_input=="delete":
                        product_names=[]
                        while True:
                            user_input=input("\npress any key continue deleting products or [exit] to go back\n>>>").lower().strip()
                            if user_input=="exit":
                                break
                            user_input=input("\nEnter product name(s) or enter [next] to proceed:\n>>>").lower().strip()
                            while True:
                                if user_input=="next":
                                    user_input=None
                                    break
                                product_names.append(user_input)
                                user_input=input(">>>").lower().strip()
                        
                            validated_product_names=sharedfunctionalities.validate_product_list(product_names)
                            if not validated_product_names:
                                continue
                            print(validated_product_names)
                            sharedfunctionalities.delete_product(validated_product_names)
                    elif user_input=="add":
                        while True:
                            product_list=[]
                            user_input=input("\npress any key continue or enter [exit] to go back\n>>>").lower().strip()
                            if user_input=="exit":
                                break
                            product_name=input("\n    Enter product Name:").lower().strip()
                            price=int(input("    Enter product price:").lower().strip())
                            initial_quantity=int(input("    Enter product initial Quantity:").lower().strip())
                            available_quantity=int(input("    Enter product available Quantity:").lower().strip())

                            while True:                           
                                product_list.append({"product_Name": product_name,"available_Quantity": available_quantity,"price": price,"state": "","stock_level": "","initial_stock": initial_quantity})
                                user_input=input("\npress any key continue adding products or enter [next] to proceed:\n>>>").lower().strip()
                                if user_input=="next":
                                    break

                                product_name=input("    Enter product Name:").lower().strip()
                                price=int(input("    Enter product price:").lower().strip())
                                initial_quantity=int(input("    Enter product initial Quantity:").lower().strip())
                                available_quantity=int(input("    Enter product available Quantity:").lower().strip())
                            try:
                                if not product_list:
                                    raise ValueError("no product to add!")
                                sharedfunctionalities.add_product(product_list)
                                product_list=[]
                            except ValueError as e:
                                print(e)
                                         
              
            if user_input=="customers":
                print("\n\n--------customer management pannel--------")
                while True:
                    user_input=input("\n    1. search for a given customer by username\n    2. viewcustomers\n    3. suspend account\n(searchcustomer/allcustomers/suspend/exit)\n>>>").lower()
                    if user_input=="exit":
                                break
                    
                    if user_input=="searchcustomer":
                        user_input=input("\n    Enter customer username:\n")
                        sharedfunctionalities.search_Entityby_Name(user_input, entity_Type="customer" ,Who=entity_type)
                        continue
                    if user_input=="allcustomers":
                        sharedfunctionalities.display_Entity( entity_Type="customer",single_Entity=False ,Who=entity_type)
                        continue 
                    if user_input=="suspend":
                        user_name=input("\nEnter user name whose account is to be suspended\n>>> ")
                        sharedfunctionalities.suspend_account(user_name)
                        continue
                
                 
            elif user_input=="maketransactions":
                
                print("\n\n--------Transaction management pannel--------")
                
                while True:
                    input("\n    1. buy product(s)\n    2. deposit\n    3. checkbalance(s)\n(buy/deposit/balance/exit)\n").lower() 
                    if user_input=="exit":
                                break
                    
                    if user_input=="buy":
                        user_input=input("\n    Enter customer username:\n")
                        sharedfunctionalities.search_Entityby_Name(user_input, entity_Type="customer" ,Who=entity_type)
                        continue
                    if user_input=="deposit":
                        sharedfunctionalities.display_Entity( entity_Type="customer",single_Entity=False ,Who=entity_type)
                        continue 
                    
                    if user_input=="buy":
                        
                        while True:
                            product_list=[]
                            user_input=input("\npress any key continue or enter [exit] to go back\n>>>").lower().strip()
                            if user_input=="exit":
                                break
                            product_name=input("\n    Enter product Name:").lower().strip()  
                            quantity=int(input("    Enter product Quantity:").lower().strip())

                            while True:                           
                                product_list.append({"product_Name": product_name,"Quantity": quantity})
                                user_input=input("\npress any key continue adding products or enter [next] to proceed:\n>>>").lower().strip()
                                if user_input=="next":
                                    break

                                product_name=input("\n    Enter product Name:").lower().strip()  
                                quantity=int(input("    Enter product Quantity:").lower().strip())
                            try:
                                if not product_list:
                                    raise ValueError("no product to add!")
                                sharedfunctionalities.purchase_item(product_list)
                                product_list=[]
                            except ValueError as e:
                                print(e)
                            
                    
                    if user_input=="exit":
                        break
                    else:
                        print("invalid input!")
                        continue
            