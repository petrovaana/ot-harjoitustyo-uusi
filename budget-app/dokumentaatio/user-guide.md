# User Guide:



Download the latest release of the Application.



### Configuration:

The application uses a local SQLite database. To initialize the database, run initialize\_database.py, which will execute the SQL commands in schema.sql to create the necessary tables. Make sure your DATABASE\_FILENAME in your .env -file is the following:



DATABASE\_FILENAME=database.sqlite



### Starting the Application:



Install dependencies before running the application, with poetry install. Now you can run the application with poetry run invoke start.



### Beginning with the application:



#### Create an Account:

Firstly you have to create an account, and use a name thats at least 3 letters long and a password that is at least 8 letters long. Then press the button create the account and if it takes you to login view, the account has been created.



#### Login:

Type your existing account and password, and press button login. It should take you to a view where you can log your spendings and incomes. The page also has a summary of all of them.



#### Logging in transactions:

You can log in transactions by pressing buttons, and writing down the context and amount and then pressing to submit it.

