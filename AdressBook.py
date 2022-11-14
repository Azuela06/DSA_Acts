
def sublist_contains(lst: list, obj: str) -> bool: #Checking the item if it is within the sublist
    for item in lst:
        try:
            if obj in item:
                return True
        except TypeError:
            pass
    return False

addressBook: list[str] = []

i: int
for i in range(50):
    while True: 
        print("\t ---ADDRESS BOOK MENU--- \t")
        option: int = int(input("What do you wish to do? \n 1.Add new contact \n 2.Edit Contact \n 3.Delete Contact \n 4.View Contact \n 5.Search Address Book \n 6.Exit \n Enter an option(should be number): ")) 
        """
        retrieves an input from the user
        """
        if option == 1: #Add new Contact 
            _name: str = input("Enter first name here: ")
            _surname: str = input("Enter last name here: ")
            address: str = input("Enter address here: ")
            phone:str = input("Enter phone number here: ")
            _confirm: str = input("Are you sure you want to add this contact in the book?\n (answerable by y or Y): ")
            """
            prompts the user to confirm if they want
            to add the new contact to the Address Book
            """
            if _confirm == 'y' or _confirm == 'Y': 
                addressBook.append([_surname,_name, address, phone]) 
                """
                Storing the details as a sublist within the list.
                """
                print("\tContact added succesfully!\t")
                print("\t\t ---ADDRESS BOOK--- \t\t")
                print(f"\t {addressBook} \t")
            else:
                print("\t Add request canceled. \t")
        elif option == 2: #Edit Contact
            _name: str = input("Enter the name of an existing contact you want to modify: ")
            _surname: str = input("Enter the new surname: ")
            address: str = input("Enter new address: ")
            phone: str = input("Enter new phone number: ")
            _confirm: str = input("Are you sure you want to edit this contact in the book?\n (answerable by y or Y): ")
            if _confirm == 'y' or _confirm == 'Y':
                item: str 
                for item in addressBook:
                    if item[1] == _name:
                        item[2] = address
                        item[3] = phone
                        item[0] = _surname
                        print("Contact Updated!")
                        print("\t\t ---ADDRESS BOOK--- \t\t")
                        print(f"\t {addressBook} \t")
                        break
                    else:
                        print("Contact not found!")
        elif option == 3: #Delete Contact
            _name: str = input("Enter the name of an existing contact you want to delete:")
            if sublist_contains(addressBook,_name) == True:
                confirm: str = input("Sure you want to delete this contact?\n (answerable by y or Y): ")
                if confirm == 'y' or confirm == 'Y':
                    index: int = [_name in a for a in addressBook].index(True) #Checking the index of the sublist
                    addressBook.pop(index)
                    print("Contact deleted!")
                    print(addressBook)
                else:
                    print("Deletion canceled.")
            else:
                print(f"{_name} is not found in the Address Book.")
        elif option == 4: #View Contact
            print("---Contact list---")
            print('['+ ',\n '.join(str(cont) for cont in addressBook) + ']') #For viewing the contact in an organized way.
        elif option == 5: # Search the address book
            _option: str = input("""Enter search \n (a) by first name \n (b) by last name \n 
            (c) by address \n (d) by contact number \n Select an option: """) #in case the user forgot other details
            if _option == 'a': #for those who remembered the first name
                _name: str = input("Enter the first name of the person you are searching for: ")
                if sublist_contains(addressBook,_name) == True: 
                    matching: list[str] = [elem for elem in addressBook if _name in elem]
                    print(matching)
                else:
                    print(f"There is no {_name} inside the address book.")
            elif _option == 'b': #for those who remembered the last name
                _surname: str = input("Enter the last name of the person you are searching for: ")
                if sublist_contains(addressBook,_surname) == True: 
                    matching: list[str] = [elem for elem in addressBook if _surname in elem]
                    print(matching)
                else:
                    print(f"There is no {_surname} inside the address book.")
            elif _option == 'c': #for those who wants to search by address
                address: str = input("Enter the address of the person you are searching for: ")
                if sublist_contains(addressBook,address) == True: 
                    matching: list[str] = [elem for elem in addressBook if address in elem]
                    print(matching)
                else:
                    print(f"There is no {address} inside the address book.")
            elif _option == 'd': #for those who want to search by the number provided
                phone: str = input("Enter the phone number of the person you are searching for: ")
                if sublist_contains(addressBook, phone) == True: 
                    matching: list[str] = [elem for elem in addressBook if phone in elem]
                    print(matching)
                else:
                    print(f"There is no {phone} inside the address book.")
            else:
                print("Search canceled.")
        else: # Option 6 or exiting the program
            print("\t Exited successfully \t") #confirmation if the program is already closed.
            break
    break
