# Xintao nian Terminal App T1A3

---
### Git repo
This is the link to my ***[GitHub Repo](https://github.com/Nianxintao/Xintaonian_T1A3Xintaonian_T1A3/tree/master)***

---
### Trello Board
This is the link to my ***[TrelloBoard](https://trello.com/u/johnnian1/boards)***

---

## App Usage
### Dependencies

---
This terminal app requires Python 3 to be installed on your local machine.

All other dependency is installed by virtual env.

---
### How to run the app

---
1. Navigate to the /src directory
2. Run the bash script ./run.sh

---
## About the app

### main page 
The main page is for users to choose the features of the app
1. Recording income & expenses
2. Editing income & expenses
3. Remove income & expenses
4. Review income & expenses
5. Exit

Please see the img below:

![main.png](doc%2Fmain.png)

---

The app will be greeting the users and inform all users to add '-'in front of the expenses.

---

### Feature 1 Recording  income & expenses
This feature is allowing users to input the amount of income or expenses, and also record
the type of the input. examples:

![main2.png](doc%2Fmain2.png)

![main3.png](doc%2Fmain3.png)

![Func1.png](doc%2FFunc1.png)

The app will print a success or fail message depending on the input. If the user succeed it will print 
Information has been added successfully！

If you put 'str' in amount section the app will inform you as follows:

![main4.png](doc%2Fmain4.png)

The input data will be a list of inputs given by the user and will be validate as the first step.

1. Read record from the csv
2. Create a new record and add to the list
3. Write the new record to the csv

---
### Feature 2 Editing  income & expenses
This feature is allowing users to edit the category or amount of income or expenses, and also record
the new input. examples:

![main5.png](doc%2Fmain5.png)

![Func2.png](doc%2FFunc2.png)

The app will print a success or fail message depending on the input. If the user succeed it will print 
Editing done!!

The input data will be a list of inputs given by the user and will
be validate as the first step. The update feature will

1. Read records from the csv
2. Find the record to update using the row number give by the user
3. Update the record category and amount
4. Write the changed editing back to the csv file
---

### Feature 3  Remove income & expenses
When removing records, the app asks to enter the row number to be deleted.
Example as below:

![main6.png](doc%2Fmain6.png)

![Func3.png](doc%2FFunc3.png)

The input data will be a list of inputs given by the user and will be validate as the first step. 

1. Read records from the csv
2. Find the record  to delete using the row number give by the users
3. Remove the record from the list of expenses
4. Write the other records back to the csv file
---

### Feature 4  Review income & expenses
The user is also able to view any templates that have been created in the application.
The list gets section of category amount, date and row number.
At the end of the list. App will give users the figures of total income total expenses and total balance.
Example as below:

![main7.png](doc%2Fmain7.png)

![Func4.png](doc%2FFunc4.png)

---

### Feature 5   Exit
If the user choose 5 to exit, the app will no longer be running. Rerun ./run_app.sh

---

## Project Planning
For finish the project  I did the steps below:

1. Set up a trello board for T1A3
![Trello Board 1.jpg](doc%2FTrello%20Board%201.jpg)
![Trello Board 2.jpg](doc%2FTrello%20Board%202.jpg)
![Trello Board 3.jpg](doc%2FTrello%20Board%203.jpg)
![Trello Board 4.jpg](doc%2FTrello%20Board%204.jpg)
![Trello Board 5.jpg](doc%2FTrello%20Board%205.jpg)
![Trello Board 6.jpg](doc%2FTrello%20Board%206.jpg)
![Trello Board 7.png](doc%2FTrello%20Board%207.png)
![Trello Board 8.png](doc%2FTrello%20Board%208.png)
![Trello Board 9.png](doc%2FTrello%20Board%209.png)
![Trello Board 10.png](doc%2FTrello%20Board%2010.png)
2. Create the main.py
3. Create the Functions.py
4. Write the Recording  feature
5. Write the Editing feature
6. Write the Removing feature
7. Write the Reviewing feature
8.  Tests
9. Error Handling 

---

### Dependencies
To run this application, you must have Python 3 installed.
The application also makes use of the following dependencies which are automatically set up upon launch.
colored==2.2.3

---

## Code Style Guide
The code was written referencing the PEP 8 Style Guide for Python using the Black Code Style and 
formatter as it is PEP8 compliant.

The styles followed include:

* Lower case variables with underscores (example_variable)
* 4 Space indentation
* 2 Blank lines to separate functions
* Imports separated by lines and grouped
* Use of double quotes consistently

---


