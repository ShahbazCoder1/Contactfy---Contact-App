import mysql.connector as con
from mysql.connector import Error
import sys
from datetime import date

connection = None

# Establish Connection
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

# Setup & Launch
def setup():
    global connection
    stmt = connection.cursor()
    try:
        query = """
        CREATE TABLE IF NOT EXISTS people (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(10) NOT NULL,
            phone_no VARCHAR(10) NOT NULL,
            address VARCHAR(10) NULL,
            date DATE NOT NULL
        );
        """
        stmt.execute(query)
        connection.commit()
        print("SetUp Done!")
        print("\n+-------------------------+")
        print("| Contactfy - Contact App |")
        print("+-------------------------+\n")
    except Error as e:
        print("Error occurred at '{}' ".format(e))
        sys.exit()
    finally:
        stmt.close()

# Display all Contacts
def display():
    global connection
    print("\n+------+------------+------------+------------+------------+")
    print("| %-56s |" % "ALL CONTACTS")
    stmt = connection.cursor()
    try:
        query = "SELECT name, phone_no, address, date FROM people"
        stmt.execute(query)
        data = stmt.fetchall()
        stmt.close()
        count = 1
        print("+------+------------+------------+------------+------------+")
        print("| ID   | Name       | Phone no.  | Address    | Date       |")
        print("+------+------------+------------+------------+------------+")
        for i in data:
            print("| %4s | %-10s | %-9s | %-10s | %-10s |" % (count, i[0], i[1], i[2], i[3]))
            count +=1
        print("+------+------------+------------+------------+------------+\n")
    except Error as e:
        print("Error occurred at '{}' ".format(e))
        sys.exit()

# Add a Contact
def add():
    global connection
    stmt = connection.cursor()
    name = input("Enter the person name: ")
    ph = input("Enter the Phone number: ")
    ad = input("Enter the Address: ")
    cur_date = date.today()
    try:
        query = "INSERT INTO people (name, phone_no, address, date) VALUES ('{}', '{}', '{}', '{}')".format(name, ph, ad, cur_date)
        stmt.execute(query)
        connection.commit()
        print("Upload Done!\n")
    except Error as e:
        print("Error occurred at '{}' ".format(e))
    finally:
        stmt.close()

# Delete a Contact
def delete():
    global connection
    stmt = connection.cursor()
    ele = input("Enter the 'NAME' of the Contact Which you want to Delete: ")
    try:
        query = "DELETE FROM people WHERE LOWER(name) = LOWER('{}')".format(ele)
        stmt.execute(query)
        connection.commit()
        print("Deleted contact '{}' successfully!".format(ele))
    except Error as e:
        print("Error occurred at '{}' ".format(e))
    finally:
        stmt.close()

#Updating the Contacts
def update():
    global connection
    stmt = connection.cursor()
    ele = input("Enter the 'NAME' of the Contact Which you want to Update: ")
    print("+---------------------------------------+")
    print("| %-37s |" % "Update Type")
    print("+---------------------------------------+")
    print("| Enter '1' for updating the Name       |")
    print("| Enter '2' for Updating the Phone no.  |")
    print("+---------------------------------------+")
    ch = int(input("Enter your Choice: "))
    print("")
    if ch == 1:
        try:
            name = input("Enter the new Name: ")
            query = "UPDATE people SET name = '{}' WHERE LOWER(name) = LOWER('{}')".format(name, ele)
            stmt.execute(query)
            connection.commit()
            print("Updated contact '{}' successfully!".format(ele))
        except Error as e:
            print("Error occurred at '{}' ".format(e))
    elif ch == 2:
        try:
            ph = input("Enter the new Phone no.: ")
            query = "UPDATE people SET phone_no = '{}' WHERE LOWER(name) = LOWER('{}')".format(ph, ele)
            stmt.execute(query)
            connection.commit()
            print("Updated contact '{}' successfully!".format(ele))
        except Error as e:
            print("Error occurred at '{}' ".format(e))
    else:
        print("Invalid Choice!")
        stmt.close()
        return


#Search Contacts
def search_contacts():
    global connection
    stmt = connection.cursor()
    search_type = "name"
    print("+-----------------------------------------+")
    print("| %-39s |" % "Search Type")
    print("+-----------------------------------------+")
    print("| Enter '1' for Searching with Name       |")
    print("| Enter '2' for Searching with Phone no.  |")
    print("+-----------------------------------------+")
    ch = int(input("Enter your Choice: "))
    if ch == 2:
        search_type = "phone_no"
    ele = input("Enter the '{}' of the Contact Which you want to Search: ".format(search_type))
    try:
        query = f"SELECT name, phone_no, address, date FROM people WHERE LOWER({search_type}) = LOWER(%s)"
        stmt.execute(query, (ele,))
        data = stmt.fetchall()
        stmt.close()
        if not data:
            print("Contact not found!")
            return
        count = 1
        print("+------+------------+------------+------------+------------+")
        print("| ID   | Name       | Phone no.  | Address    | Date       |")
        print("+------+------------+------------+------------+------------+")
        for i in data:
            print("| %4s | %-10s | %-9s | %-10s | %-10s |" % (count, i[0], i[1], i[2], i[3]))
            count +=1
        print("+------+------------+------------+------------+------------+\n")
    except Error as e:
        print("Error occurred at '{}' ".format(e))
        sys.exit()

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

#run
connect()
main()