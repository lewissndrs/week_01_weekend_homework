# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(shop_name):
    return shop_name["name"]

def get_total_cash(shop_name):
    return shop_name["admin"]["total_cash"]

def add_or_remove_cash(shop_name,amount):
    shop_name["admin"]["total_cash"] += amount
    return shop_name["admin"]["total_cash"]

def get_pets_sold(shop_name):
    return shop_name["admin"]["pets_sold"]

def increase_pets_sold(shop_name, amount):
    shop_name["admin"]["pets_sold"] += amount
    return shop_name["admin"]["pets_sold"]

def get_stock_count(shop_name):
    return len(shop_name["pets"])

def get_pets_by_breed(shop_name, breed):
    pets_by_breed = []
    for pet in shop_name["pets"]:
        if pet["breed"] == breed:
            pets_by_breed.append(pet)
    return pets_by_breed

def find_pet_by_name(shop_name, name):
    for pet in shop_name["pets"]:
        if pet["name"] == name:
            return pet
    return None
 

def remove_pet_by_name(shop_name,name):
    for pet in shop_name["pets"]:
        if pet["name"] == name:
            pet["name"] = None

def add_pet_to_stock(shop_name,new_pet):
    return shop_name["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount
    return customer

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer,new_pet):
    customer["pets"].append(new_pet)
    return customer["pets"]

def customer_can_afford_pet(customer,new_pet):
    can_afford = False
    if customer["cash"] >= new_pet["price"]:
        can_afford = True
    return can_afford


# this needs to: see if customer has enough funds
# add one pet to customer
# add one to pets sold
# remove money from customer cash
# add cash to shop cash

def sell_pet_to_customer(shop_name,pet,customer):
   if (pet != None) and (customer_can_afford_pet(customer, pet) == True):
      #    sell the pet
     remove_customer_cash(customer, pet["price"])
     add_or_remove_cash(shop_name,pet["price"])
     add_pet_to_customer(customer,pet)
     remove_pet_by_name(shop_name,pet["name"])
     increase_pets_sold(shop_name,1)
#   do nothing
