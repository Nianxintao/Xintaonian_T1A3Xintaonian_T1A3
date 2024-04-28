# import Live date and time
import datetime
# import csv file module
import csv


# Define record_expense function, and pass category and amount argument from main.py
def record_expense(category, amount):
    # Python function imported. shows as Day(day of  month)/ Month(Month name, short version)/Year(Year, full version)
    date = datetime.datetime.now().strftime("%d-%b-%Y")
    # create open and self-closing a csv file named expenses in append mode. name variable as csvfile
    with open('expenses.csv', 'a', newline='') as csvfile:
        # a variable named writer assigned the result of the writing method of csv
        writer = csv.writer(csvfile)
        # enter in row in certain order
        writer.writerow([date, category, amount])


# Define edit_expense function, and pass row_num category and  amount arguments from main.py
def edit_expense(row_num, category, amount):
    # create a new python list
    rows = []
    # open the 'expenses' file in read mode name as csvfile
    with open('expenses.csv', 'r') as csvfile:
        # a variable named reader assigned the result of the reading method of csv
        reader = csv.reader(csvfile)
        # the enumerate function in Python converts a data collection object into an enumerate object(list tuple etc).
        for i, row in enumerate(reader):
            # the row number user DOES  input will be appended in the reader list.
            if i == row_num:
                # append new category and amount in selected row into new list named rows
                rows.append([row[0], category, amount])
                # the row user DOES NOT input will be appended in the new list named rows.
            else:
                rows.append(row)

    with open('expenses.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)


# Define edit_expense function, and pass row_num argument from main.py
def delete_expense(row_num):
    # create a new python list
    rows = []
    # put all previous list into the new list except the one users want to delete
    with open('expenses.csv', 'r') as csvfile:
        # a variable named reader assigned the result of the reading method of csv
        reader = csv.reader(csvfile)
        # the enumerate function in Python converts a data collection object into an enumerate object(list tuple etc).
        for i, row in enumerate(reader):
            # the row number user DOES NOT input will be appended in the reader list.
            # the row number user DO input will NOT be appended in the reader list So removed.
            if i != row_num:
                rows.append(row)
    # open the 'expenses' file in writing mode name it as csvfile.
    with open('expenses.csv', 'w', newline='') as csvfile:
        # a variable named writer assigned the result of the writing method of csvfile
        writer = csv.writer(csvfile)
        # pass the value of rows in 'writerows' function to the variable writer.
        writer.writerows(rows)


# Define view_expense function
def view_expenses():
    # Error handling for if the csvfile hasn't been created yet
    try:
        # set total_expenses = 0 as default
        total_expenses = 0
        # set total_income = 0 as default
        total_income = 0
        # open the 'expenses' file in reading mode name it as csvfile.
        with open('expenses.csv', 'r') as csvfile:
            # a variable named reader assigned the result of the reading method of csv
            reader = csv.reader(csvfile)
            # for loop
            for i, row in enumerate(reader):
                print(f"{i}. Date: {row[0]}, Category: {row[1]}, Amount: {row[2]}")
                # if the value of row[2] less than 0 --> the expenses amount
                if float(row[2]) < 0:
                    # assign the absolute value of row[2] to  variable total_expenses
                    total_expenses += abs(float(row[2]))
                    # else the value of row[2] greater than 0 --> the income amount
                else:
                    # assign the  value of row[2] to  variable total_expenses
                    total_income += float(row[2])
        #  assign  value of  total_income - total_expenses  to variable total_balance
        total_balance = total_income - total_expenses
        # show users the information as below
        print(f"Total income: {total_income}")
        print(f"Total expenses: {total_expenses}")
        print(f"Total_balance: {total_balance}")

    # Error handling triggered if the csvfile has been created yet.
    except FileNotFoundError:
        # if the csvfile not found. show users the information as below
        print("The record is not created yet!")
