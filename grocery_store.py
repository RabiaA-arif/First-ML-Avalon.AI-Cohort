#  Grocesory store requirements
# available_items: list = ["chia","sugar","elachi","oil","chawal","onion"]
item_price: dict = {"chia": 200, "sugar": 230, "elachi": 80,"oil": 750, "chawal":380,"onion":70}

user_input: str =input("Enter The Name of Item: ")
# price: int = item_price.get(user_input)
price: int = item_price[user_input]
if user_input in item_price:
    if 100 <= price <= 500:
            print("item available")
            print(price)
    
    
        


    



    

      