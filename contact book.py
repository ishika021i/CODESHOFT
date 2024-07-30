import csv
book_fields = ['name','email','phone','address']
book_database = 'book.csv'
 
 
def display_menu():
    print(""" 
  ------------------------------------------------------
 |======================================================| 
 |======== Welcome To contact book	========|
 |======================================================|
  ------------------------------------------------------""")
    print("1. Add contact")
    print("2. View contact")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Quit")
def add_contact():
    print("""
    -------------------------
    Add contact Information
    -------------------------""")
    global book_fields
    global book_database
    book_data = []
    for field in book_fields:
        value = input("Enter " + field + ": ")
        book_data.append(value)
    with open(book_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([book_data])
    print("***_____Data saved successfully_____***")
    input("Press any key to continue :")
    return
def view_contact():
    global book_fields
    global book_database
    print("--- >>>>Contact Records<<<< ---")
    with open(book_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in book_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")
        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")
    input("Press any key to continue :")
def search_conatct():
    global book_fields
    global book_database
    print("--- >>>>Search contact<<<< ---")
    name = input("Enter name to search: ")
    with open(book_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if name == row[0]:
                    print("-----***** Contact Found *****-----")
                    print("Name: ", row[0])
                    print("Email: ", row[1])
                    print("Phone no.: ", row[2])
                    print("Address ", row[3])
                    break
        else:
            print("name not found in our database")
    input("Press any key to continue :")
def update_contact():
    global book_fields
    global book_database
    print("--- >>>>Update Contact<<<< ---")
    name = input("Enter name to update: ")
    index_contact = None
    updated_data = []
    with open(book_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if name == row[0]:
                    index_contact = counter
                    print("conatct Found: at index ",index_contact)
                    contact_data = []
                    for field in book_fields:
                        value = input("Enter " + field + ": ")
                        contact_data.append(value)
                    updated_data.append(contact_data)
                else:
                    updated_data.append(row)
                counter += 1
    if index_contact is not None:
        with open(book_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("name not found in our database")
 
    input("Press any key to continue :")
 
 
def delete_contact():
    global book_fields
    global book_database
 
    print("--- >>>>Delete contact<<<< ---")
    name = input("Enter name to delete: ")
    contact_found = False
    updated_data = []
    with open(book_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if name != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    contact_found = True
 
    if contact_found is True:
        with open(book_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("Name :", name, "deleted successfully")
    else:
        print("name not found in our database")
 
    input("Press any key to continue :")
 
while True:
    display_menu()
 
    choice = input("Enter your choice: ")
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contact()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    else:
        break
 
print("""
-------------------------------
Thank you for using our system
-------------------------------""")
