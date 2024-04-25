import datetime
import csv


def record_expense(category, amount):
    date = datetime.datetime.now().strftime("%d-%b-%Y")
    with open('expenses.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([date, category, amount])


def edit_expense(row_num, category, amount):
    rows = []
    with open('expenses.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i == row_num:
                rows.append([row[0], category, amount])
            else:
                rows.append(row)

    with open('expenses.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)


def delete_expense(row_num):
    rows = []
    with open('expenses.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i != row_num:
                rows.append(row)

    with open('expenses.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)


def view_expenses():
    total_expenses = 0
    total_income = 0
    with open('expenses.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            print(f"{i}. Date: {row[0]}, Category: {row[1]}, Amount: {row[2]}")
            if float(row[2]) < 0:
                total_expenses += abs(float(row[2]))
            else:
                total_income += float(row[2])

    total_balance = total_income - total_expenses

    print(f"Total income: {total_income}")
    print(f"Total expenses: {total_expenses}")
    print(f"Total_balance: {total_balance}")