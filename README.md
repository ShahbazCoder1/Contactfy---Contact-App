# Contactfy - A Simple Contact Management App

This Python application is a basic contact management system designed to store, retrieve, update, and delete contact information. It utilizes a MySQL database to persist the data.

## Features

* **Add Contacts:** Add new contact entries with name, phone number, address, and date.
* **View Contacts:** Display all stored contacts in a user-friendly table format.
* **Update Contacts:** Modify existing contact information (name or phone number).
* **Delete Contacts:** Remove contact entries.
* **Search Contacts:** Search for contacts by name or phone number.

## Screenshots

<table style="width:100%;">
  <tr>
    <td style="width:33.33%;"><img src="https://github.com/ShahbazCoder1/Contactfy---Contact-App/blob/main/Screenshots/Screenshot%202024-05-25%20102504.png" alt="Screenshot 1" style="width:100%; height:auto;"/></td>
    <td style="width:33.33%;"><img src="https://github.com/ShahbazCoder1/Contactfy---Contact-App/blob/main/Screenshots/Screenshot%202024-05-25%20102549.png" alt="Screenshot 2" style="width:100%; height:auto;"/></td>
    <td style="width:33.33%;"><img src="https://github.com/ShahbazCoder1/Contactfy---Contact-App/blob/main/Screenshots/IMG_20240525_112900.jpg" alt="Screenshot 3" style="width:100%; height:auto;"/></td>
  </tr>
</table>

## Setup

1. **Install MySQL:** Ensure you have MySQL installed on your system.
2. **Create a Database:** Create a new database named "Contact" in your MySQL instance.

   ```bash
   create database Contact;
4. **Install Python Packages:** Install the necessary Python packages:
   ```bash
   pip install mysql-connector-python

5. **Configure Credentials:** In the provided Python code, replace the placeholder values for host, user, password, and database with your actual MySQL database credentials.

## Running the Application
1. **Save the Code:** Save the provided Python code as a file named `main.py`.
2. **Execute the Code:** Run the script from your terminal:

   ```bash
   python main.py
3. **Interact with the Menu:** Follow the on-screen menu options to add, update, delete, search, or view contacts.

## Code Breakdown
The provided Python code is structured as follows:
1. **Imports:**
   
   ```python
   import mysql.connector as con
   from mysql.connector import Error
   import sys
   from datetime import date
   ```

   - mysql.connector: This library is used for connecting to and interacting with the MySQL database.
   - sys: This module provides access to system-specific parameters and functions.
   - datetime: This module is used for working with dates.

2. **Global Connection:**
   
   ```python
   connection = None
   ```
   
   - A global variable connection is initialized to store the connection object to the MySQL database.

3. **Connect Function:**

   ```python
   def connect():
      global connection
       try:
         connection = con.connect(
            host="localhost",
            user="root",
            password="123456",
            database="Contact"
           )
         print("Connected!")
         setup()
      except Error as e:
         print("The error '{}' ".format(e))
        sys.exit()
   ```   
   - Establishes a connection to the MySQL database.
   - Uses the provided credentials to connect.
   - Calls the setup function after successful connection.

4. **Setup Function:**

   ```python
   query = """
        CREATE TABLE IF NOT EXISTS people (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(10) NOT NULL,
            phone_no VARCHAR(10) NOT NULL,
            address VARCHAR(10) NULL,
            date DATE NOT NULL
        );
        """
   ```

   - Creates the people table in the database if it doesn't already exist.
   - Defines the table structure with columns for `id`, `name`, `phone_no`, `address`, and `date`.
      
5. **Other Functions:**
   
   - `display()`: Displays all contacts stored in the database.
   - `add()`: Adds a new contact to the database.
   - `delete()`: Deletes a contact from the database.
   - `update()`: Updates existing contact information.
   - `search_contacts()`: Searches for contacts by name or phone number.
  
6. **Main Function:**

   ```python
   # Main Function
   def main():
       while True:
           print("+-----------------------------------+")
           print("| %-33s |" % "Menu")
           print("+-----------------------------------+")
           print("| Enter '1' for Adding a Contact    |")
           print("| Enter '2' for Updating a Contact  |")
           print("| Enter '3' for Searching a Contact |")
           print("| Enter '4' for Deleting a Contact  |")
           print("| Enter '5' for Viewing All Contact |")
           print("+-----------------------------------+")
           ch = int(input("Enter your Choice: "))
           print("")
           if ch == 1:
               while True:
                   add()
                  fr = input("Do you want to ENTER more Contacts ('Y' or 'N'):")
                   if fr.lower() == 'n':
                       break
           elif ch == 2:
               while True:
                   update()
                   fr = input("Do you want to UPDATE more Contacts ('Y' or 'N'):")
                   if fr.lower() == 'n':
                       break
           elif ch == 3:
               while True:
                   search_contacts()
                   fr = input("Do you want to SEARCH more Contacts ('Y' or 'N'):")
                   if fr.lower() == 'n':
                       break
           elif ch == 4:
               while True:
                   delete()
                   fr = input("Do you want to DELETE more Contacts ('Y' or 'N'):")
                   if fr.lower() == 'n':
                       break
           elif ch == 5:
               display()
           else:
               print("The End!")
               sys.exit()
   ```

   - The `main()` function serves as the main execution loop for the application.
   - It presents the menu options to the user and calls the appropriate functions based on user input.

7. **Running the Code:**

   - The `connect()` function is called to establish a connection to the database.
   - The `main()` function is called to start the application.
   
## Conclusion
This simple contact management application demonstrates how to use Python to interact with a MySQL database for basic data storage and manipulation. It provides a foundation for building more complex contact management applications with features like search filtering, data visualization, and user authentication.
