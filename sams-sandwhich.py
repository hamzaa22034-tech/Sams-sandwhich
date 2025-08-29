
def bread_selection():
    breads = ["White", "Brown", "Italian", "Granary"]

    print("We have the following breads:")
    for i, bread in enumerate(breads): #prints out each item on the list
        print(f"{i+1}. {bread}")
    print()

    bread_selected=int(input("Which bread did you want? Enter a number:")) 
    return breads[bread_selected - 1] #returns back a string

def meat_selection():
    meats = ["Beef", "Chicken", "Fish", "Pork", "No Meat"]

    print("We have the following meats:")
    for i, meat in enumerate(meats): #prints out each item on the list
        print(f"{i+1}. {meat}")
    print()

    meat_selected=int(input("Which meat did you want? Enter a number:")) 
    return meats[meat_selected - 1] #returns back a string

def cheese_selection():
    cheeses = ["Cheddar", "Mozzarella", "Gouda", "Brie", "No Cheese"]

    print("We have the following cheeses:")
    for i, cheese in enumerate(cheeses): #prints out each item on the list
        print(f"{i+1}. {cheese}")
    print()

    cheese_selected=int(input("Which cheese did you want? Enter a number: ")) 
    return cheeses[cheese_selected - 1] #returns back a string

def salad_selection():
    ingredients = ["Lettuce", "Tomato", "Carrot", "Cucumber", "Onions"]
    selected_ingredients = []

    print("Please choose the ingredient you want: \n")

    for ingredient in ingredients:
        choice = str(input(f"Would you like {ingredient} (y/n): "))
        if choice == "y":
            selected_ingredients.append(ingredient)


    return selected_ingredients






def dressing_selection():
    dressingss = ["Ranch", "Caesar", "Italian Dressing", "Honey Mustard", "No dressings"]

    print("We have the following dressingss:")
    for i, dressings in enumerate(dressingss): #prints out each item on the list
        print(f"{i+1}. {dressings}")
    print()

    dressings_selected=int(input("Which dressings did you want? Enter a number: ")) 
    return dressingss[dressings_selected] #returns back a string


#main program
print("Welcome to Sam's Sandwhich Shop")

#creating a variable that calls up the choice functions and returns their choice
bread_choice=bread_selection()
meat_choice=meat_selection() 
cheese_choice=cheese_selection()
salad_choice=salad_selection()
dressing_choice=dressing_selection()

print(f"""
_____________Your Order____________
    bread choce: {bread_choice}
    meat choce: {meat_choice}
    cheese choce: {cheese_choice}
    salad choce: {salad_choice}
    dressing choce: {dressing_choice}
_____________End Order____________
""")