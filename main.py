# Show the greeting to users when the app runs
print("Thanks to choosing us for your Expenses Recording")

# When the app is running in terminal set it as true
running = True
while running:
    # when the app is running show option 1 as Recording the expenses
    print("1. Recording expenses")

    # when the app is running show option 2 as Editing Expenses
    print("2. Editing Expenses")

    # when the app is running show option 3 as Recording the expenses
    print("3. Remove Expenses")

    # when the app is running show option 4 as Review the expenses
    print("4. Review Expenses")

    # when the app is running show option 5 as End the app
    print("5. Exit")

    # name variable as choice and allow users to make their own option using input function
    choice = input("Please choose your option：")
