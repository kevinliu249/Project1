import time

def expense_list():
    for n in category_dict:
        print(f"{n}: {category_dict[n]} \n")


def add_category():
    cat_name = input("Type the name of the category or '0' to go back: ")
    if cat_name == "0":
        return
    elif cat_name in category_dict:
        print("Category already made. Name a new category. \n")
    else:
        category_dict[cat_name] = 0
        print(f'Category {cat_name} successfully added.\n')
        expense_list()


def add_expense():
    category = True
    while category is True:
        cat_to_add = input("Type the category name desired to add expense value or '0' to go back: ")
        if cat_to_add == "0":
            return
        elif cat_to_add in category_dict:
            amount = input(f"Category {cat_to_add} selected, input the number amount: $ ")
            try:
                category_dict[cat_to_add] += int(amount)
                print(f"${amount} added to {cat_to_add}.\n")
                expense_list()
                category = False
            except ValueError:
                print("That was not a valid number, please try again.\n")
        else:
            print(f"{cat_to_add} not found in expense categories, please try again.\n")

def calc_sum():
    sum = 0
    for n in category_dict:
        sum += category_dict[n]
    return sum




print("Welcome to the Monthly Expense Tracker App! \n \n"
      "Instructions: \n"
      " -Start by adding an expense category \n"
      " -(Once you have categorie(s) set up, you can add amount to each category) \n"
      " -You may have the total summary of your expenses calculated at any time!\n"
      " -Contact the developer @XYZ for further questions. \n \n"
      "Functions:\n"
      " 0. Home Screen\n"
      " 1. Add Category\n"
      " 2. Input Expense\n"
      " 3. Calculate Sum \n")

category_dict = {}

while True:
    user_action= input("\n"
                       "Choose an action (Type 1, 2, 3 for corresponding function, or 0 to go to home): "
                       )
    if user_action == "1":
        add_category()
    elif user_action == "2":
        add_expense()
    elif user_action == "3":
        print(f"\nTotal summary of expenses: ${calc_sum()}.")




