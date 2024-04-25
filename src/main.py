# import all functions from function.py file
from functions import record_expense, edit_expense, delete_expense, view_expenses

# code loop
running = True
# when code looping
while running:
    # add space line
    print()
    # show all the information and options as below
    print("Thanks for choosing the income and expenses recording app! the options as below: ")
    print()
    print("1. Recording income & expenses")
    print("2. Editing income & expenses")
    print("3. Remove income & expenses")
    print("4. Review income & expenses")
    print("5. Exit")
    # add space line
    print()
    print("!!! For expenses please add ' - ' before the amount")
    # add space line
    print()
    # name variable 'choice' and assign users input to the variable
    choice = input("Please choose your option：")

    # when users input is 1
    if choice == "1":
        # show which function users has chose
        print("You have chosen Recording income & expenses")
        # name variable 'category' and assign users input to the variable
        category = input("The Category of income & expenses：")
        # name variable 'amount' and assign users input to the variable, and convert the input from str to float
        amount = float(input("The expenses amount："))
        # call the function from function.py
        record_expense(category, amount)
        # function execute successfully
        print("Information has been added successfully！")

    # when users input is 2
    elif choice == "2":
        # show which function users has chose
        print("You have chosen Editing income & expenses")
        # name variable 'amount' and assign users input to the variable, and convert the input from str to int
        row_num = int(input("Please enter the record number you want edit："))
        # name variable 'category' and assign users input to the variable
        category = input("Please enter the new category：")
        # name variable 'amount' and assign users input to the variable, and convert the input from str to float
        amount = float(input("Please enter the new amount："))
        # call the function from function.py
        edit_expense(row_num, category, amount)
        # function execute successfully
        print("Editing done!!")

    # when users input is 3
    elif choice == "3":
        # show which function users has chose
        print("You have chosen Remove income & expenses")
        # name variable 'amount' and assign users input to the variable, and convert the input from str to int
        row_num = int(input("Please enter the record number you want delete："))
        # call the function from function.py
        delete_expense(row_num)
        # function execute successfully
        print("Information has been removed")

    # when users input is 4
    elif choice == "4":
        # show which function users has chose
        print("Please review the income & expenses：")
        # call the function from function.py
        view_expenses()

    # when users input is 5
    elif choice == "5":
        # show which function users has chose
        print("Exit !!!")
        # loop end
        running = False

    # when users input other than 1,2,3,4,5
    else:
        # inform the users to select from the only 5 options
        print("Please choose from the below options! ")