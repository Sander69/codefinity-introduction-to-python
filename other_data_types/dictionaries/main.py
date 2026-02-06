grocery_inventory = {"Milk":(113,"Dairy"),"Eggs":(116,"Dairy"),"Bread":(117,"Bakery"),"Apples":(141,"Produce")}

bread_details = grocery_inventory.get("Bread")
print("Details of Bread:",bread_details)

new_item = {"Cookies":(143,"Bakery")}
grocery_inventory.update(new_item)
print("Inventory after adding Cookies:", grocery_inventory)

grocery_inventory.pop("Eggs")
print("Inventory after removing Eggs:", grocery_inventory)