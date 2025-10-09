from datetime import datetime
#This function will allow the user to enter only a vaild string
def force_string(message, lower, upper):
    # infinite loop that breaks once a vaild string is given by the input
    while True: 
        string = str(input(f"{message}"))
        if len(string) >= lower and len(string) <= upper and string.isalpha():
            break #breaks loop if the above condition
        else:
            print("Invalid string")
    return string

#This function will allow the user to enter in a number
def force_integer(message, lower, upper):
    # infinite loop that breaks once a vaild integer is given by the input
    while True: 
        try: 
            integer = int(input(f"{message}"))
            if integer >= lower and integer <= upper:
                return integer
            else:
                print(f"Invalid integer, integer has to be between {lower}-{upper}")
        except ValueError:
            print("Invalid integer")

def force_phone_number(message, lower, upper):
    # infinite loop that breaks once a vaild string is given by the input
    while True: 
        string = str(input(f"{message}")).title()
        if len(string) >= lower and len(string) <= upper and string.isnumeric():
            return string
        else:
            print(f"Invalid phone number, please ensure its betweeen {lower}-{upper}")


#main program
first_name=force_string("Please enter your first name (2-15): ", 2, 15).title()
last_name=force_string("Please enter your last name (2-35): ", 2, 35).title()
phone_number=force_phone_number("Please enter your phone number (8-9): ", 8, 12)

def bread_selection():
    breads = ["White", "Brown", "Italian", "Granary"]

    print("We have the following breads:")
    for i, bread in enumerate(breads): #prints out each item on the list
        print(f"{i+1}. {bread}")
    print()

    bread_selected=force_integer("Which bread did you want? Enter a number:",1, len(breads)) 
    return breads[bread_selected - 1] #returns back a string

def meat_selection():
    meats = ["Beef", "Chicken", "Fish", "Pork", "No Meat"]

    print("We have the following meats:")
    for i, meat in enumerate(meats): #prints out each item on the list
        print(f"{i+1}. {meat}")
    print()

    meat_selected=force_integer("Which meat did you want? Enter a number:", 1, len(meats))
    return meats[meat_selected - 1] #returns back a string

def cheese_selection():
    cheeses = ["Cheddar", "Mozzarella", "Gouda", "Brie", "No Cheese"]

    print("We have the following cheeses:")
    for i, cheese in enumerate(cheeses): #prints out each item on the list
        print(f"{i+1}. {cheese}")
    print()

    cheese_selected=force_integer("Which cheese did you want? Enter a number: ", 1, len(cheeses)) 
    return cheeses[cheese_selected - 1] #returns back a string

def salad_selection():
    ingredients = ["Lettuce", "Tomato", "Carrot", "Cucumber", "Onions"]
    selected_ingredients = []

    print("Please choose the ingredient you want: \n")

    for ingredient in ingredients:
        choice = force_string(f"Would you like {ingredient} (y/n): ", 1,2)
        if choice == "y":
            selected_ingredients.append(ingredient)


    return selected_ingredients

def dressing_selection():
    dressingss = ["Ranch", "Caesar", "Italian Dressing", "Honey Mustard", "No dressings"]

    print("We have the following dressingss:")
    for i, dressings in enumerate(dressingss): #prints out each item on the list
        print(f"{i+1}. {dressings}")
    print()

    dressings_selected=force_integer("Which dressings did you want? Enter a number: ", 1, len(dressings)) 
    return dressingss[dressings_selected] #returns back a string

# function to save to file 
def save_to_file(first_name, last_name, phone_number, choices):
    with open('sams_sandwhich.txt', "a") as order_file:

        order_file.write("__________ORDER__________\n")
        order_file.write(f"First Name: {first_name} {last_name}\n") 
        order_file.write(f"Phone Number: {phone_number}\n") 
        order_file.write(f"Bread choce: {choices['bread_choice']}\n") 
        order_file.write(f"Meat choce: {choices['meat_choice']}\n")
        order_file.write(f"Salad choce: { ', '.join(choices['salad_choice']) }\n")
        order_file.write(f"Dressing choce: {choices['dressing_choice']}\n") 
        order_file.write(f"Time Booked: {datetime.today()}\n") 
        order_file.write("___________END___________\n\n")

#main program
print("Welcome to Sam's Sandwhich Shop")

choices = {
    "bread_choice":bread_selection(),
    "meat_choice":meat_selection(),
    "cheese_choice":cheese_selection(),
    "salad_choice":salad_selection(),
    "dressing_choice":dressing_selection(),
}

print(f"""
_____________{first_name} - {phone_number}_____________
    bread choce: {choices['bread_choice']}
    meat choce: {choices['meat_choice']}
    cheese choce: {choices['cheese_choice'] }
    salad choce: { ', '.join(choices['salad_choice'])}
    dressing choce: {choices['dressing_choice']}
_____________{datetime.now()}____________
""")

save_to_file(first_name, last_name, phone_number, choices)