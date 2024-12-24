import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect('AddressBook.db')
sqlcur = connection.cursor()

# Define a while loop
num_of_iteration = True

while num_of_iteration:
    # Search for someone in the address book
    def show_someone():
        print("Enter the name of the person you want to see details for:")
        person_name = str(input("> "))

        # Execute a parameterized query to retrieve the person's information
        sqlcur.execute("SELECT * FROM Peoples_Info WHERE name = ?", (person_name,))
        person_details = sqlcur.fetchone()

        if person_details:
            print(f"Name: {person_details[0]}")
            print(f"Phone Number: {person_details[1]}")
            print(f"Address: {person_details[2]}")
            print(f"Note: {person_details[3]}")
        else:
            print(f"No details found for {person_name}.")

    # Delete a person from the database
    def delete_person():
        print("What is the name of the person you want to delete?")
        person_for_deleting = str(input(">"))
        sqlcur.execute("DELETE FROM Peoples_Info WHERE name = ?", (person_for_deleting,))
        connection.commit()
        print(f"{person_for_deleting} has been deleted.")

    # Add someone to the address book
    def add_someone():
        print("What is the name of the person you want to add?")
        Persons_Name = str(input("> "))

        print("What is the phone number of the person you want to add?")
        # Ensure valid phone number input
        while True:
            try:
                Persons_Phone_Number = int(input("> "))
                break
            except ValueError:
                print("Please enter a valid phone number.")

        print("What is the address of the person you want to add?")
        Persons_Address = str(input("> "))

        print("Do you want to add a note about the person (y/n)?")
        Persons_Opinion = str(input("> "))

        if Persons_Opinion == "y":
            print("Write your note down below.")
            Persons_Note = str(input("> "))
        else:
            Persons_Note = ""

        try:
            sqlcur.execute("""INSERT INTO Peoples_Info (name, phone_number, address, note) 
                               VALUES(?, ?, ?, ?)""", 
                               (Persons_Name, Persons_Phone_Number, Persons_Address, Persons_Note))
            connection.commit()
            print("You successfully added an account.")
        except sqlite3.Error as e:
            print(f"Error inserting data: {e}")

    # The script to run
    print(" ")
    print("""Do you want to add a new person to the address book (to select this type 'add person'), 
    see details of an existing person (to select this type 'see details') 
    or delete a person from the address book (to select this type 'delete person')?(e to exit)""")
    ans = str(input(">")).strip().lower()

    if ans == "add person":
        add_someone()

    elif ans == "see details":
        show_someone()

    elif ans == "delete person":
        delete_person()

    elif ans == "e":
        print("The program has been closed.")
        num_of_iteration = False

# Close the database connection when done
connection.close()
