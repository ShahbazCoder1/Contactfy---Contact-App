# Contactfy - A Simple Contact Management App

This Python application is a basic contact management system designed to store, retrieve, update, and delete contact information. It utilizes a MySQL database to persist the data.

## Features

* **Add Contacts:** Add new contact entries with name, phone number, address, and date.
* **View Contacts:** Display all stored contacts in a user-friendly table format.
* **Update Contacts:** Modify existing contact information (name or phone number).
* **Delete Contacts:** Remove contact entries.
* **Search Contacts:** Search for contacts by name or phone number.


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
1. **Save the Code:** Save the provided Python code as a file named main.py.
2. **Execute the Code:** Run the script from your terminal:

   ```bash
   python contactfy.py
3. **Interact with the Menu:** Follow the on-screen menu options to add, update, delete, search, or view contacts.

## Code Breakdown
The provided Python code is structured as follows:
1. **Imports:**


- mysql.connector: This library is used for connecting to and interacting with the MySQL database.
- sys: This module provides access to system-specific parameters and functions.
- datetime: This module is used for working with dates.
