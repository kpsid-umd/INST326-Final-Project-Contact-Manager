# This program is a contact manager that will allow users to manage their contacts
# by adding, editing, and removing contacts. Each contact will list important information
# like the contact's name, phone number, and email address.

# Group Members: Siddharth Padithaya, Rayan Shah, and Raymond Dickscheid
import json
class User:
    """ This class stores information related to the user with methods such as adding user info, editing user info and displaying user info. 
    Attributes:
        name (str): The name of the user
    """
    def __init__(self, name):
        """ Initializes a User instance with a name
        Args:
            name(str): The name of the current user. 
        """
        self.name = name
        
    def display_user_info(self):
        """Returns the user's name
        Args:
            None
        Returns: 
            str: The user's name as an fstring
        """
        return f"Name: {self.name}"
        
    def edit_user_name(self, new_user_name):
        """ Allows the user to edit their name and change it to a new name
        Args:
            new_user_name (str): the new name of the user
        Returns:
            None
        Side Effects:
            Updates the user's name with their new name
        """
        self.name = new_user_name
        

class Contact:
    """ This class stores the contact's information such as name, phone number, and email address. It also allows the user to update the contact's information and get the contact's information.
    Attributes:
        name (str): The name of the contact
        phone_number (str): The phone number of the contact
        email (str): The email address of the contact
    """
    def __init__(self, name, phone_number, email):
        """ Initializes the contact with a name, phone number, and email address.
        Args:
            name (str): The name of the contact
            phone_number (str): The phone number of the contact
            email (str): The email address of the contact
        Returns:
            None
        Side Effects:
            Initializes the contact with a name, phone number, and email address. 
        """
        self.name = name
        self.phone_number = phone_number
        self.email = email
        
    def update_info(self, name=None, phone_number=None, email=None):
        """Allows the user to update the contact's information such as name, phone number, and email address.
        Args:
            name (str): The new name of the contact
            phone_number (str): The new phone number of the contact
            email (str): The new email address of the contact
        Returns:
            None
        Side Effects:
            Updates the contact information with a new name, phone number, and email address. If none of the parameters are added, the contact information will stay the same.
        """
        if name:
            self.name = name
        if phone_number:
            self.phone_number = phone_number
        if email:
            self.email = email
        
    def get_info(self):
        """
        Returns the contact's info such as name, phone number, and email address.
        Args:
            None
        Returns:
            str: A string with the contact's name, phone number, and email address
        """
        return f"Name: {self.name}, Phone Number: {self.phone_number}, Email: {self.email}"
        

class AddressBook:
    """
    This class stores the user's contacts and allows them to add, edit, and remove contacts from the address book.
    Attributes:
        contacts (list): A list of Contact objects that is stored in the AddressBook
    
    """
    def __init__(self):
        """ Initializes the address book with an empty list of blank contacts.
        
        """
        self.contacts = []

    def add_contact(self, contact):
        """ Adds a contact to the address book.
        Args:
            contact (Contact): The contact that needs to be added to the AddressBook
        Returns:
            None
        Side Effects:
            Adds the contact to the AddressBook. If a contact with the same name already exists, a ValueError will be raised.
        Raises:
            ValueError if a contact already exists with the same name.

        """
        for existing_contact in self.contacts:
            if existing_contact.name == contact.name:
                raise ValueError(" A contact with this name already exists. If this is a different contact, please add the last name initial to differentiate between them.")
        self.contacts.append(contact)
        self.local_save()
    
    def find_contact(self, name):
        """
        Finds a contact in the address book by name and returns the contact's information.
        Args:
            name (str): The name of the contact that needs its information found
        Returns:
            Contact: The matching contact if found. 
        Side Effects:
            If a contact with the name that was searched for is not found, a ValueError will be raised.
        Raises:
            ValueError: If the contact name could not be found in the user's contacts.
        """
        for contact in self.contacts:
            if contact.name == name:
                return contact
        raise ValueError("Contact with that name could not be found.")
    


    def edit_contact(self, name, new_name=None, new_phone_number=None, new_email=None):
        """
        Edits a contact's information in the address book
        Args:
            name (str): The name of the contact that needs to be edited
            new_name (str): The new name of the contact
            new_phone_number (str): The new phone number of the contact
            new_email (str): The new email address of the contact
        Returns:
            None
        Side Effects:
            Updates the contact's information with a new name, phone number, and email address.
        Raises:
            ValueError: If another contact already has the same name or contact could not be found.
        """
        contact = self.find_contact(name)

        if new_name:
            for names in self.contacts:
                if names.name == new_name and names != contact:
                    raise ValueError(" A contact with this name already exists.")
                
        contact.update_info(new_name, new_phone_number, new_email)
        self.local_save()



    def remove_contact(self, name):
        """
        Removes a contact from the address book
        Args:
            name (str): The name of the contact that needs to be removed
        Returns:
            None
        Side Effects:
            Removes the contact information that was searched from the AddressBook. If a contact with the name that was searched is not found, a ValueError is raised. 
        """
        contact = self.find_contact(name)
        self.contacts.remove(contact)
        self.local_save()



    def export_contacts(self, filename):
        """ Exports the contacts in the address book to a file
        Args:
            filename (str): The name of the file the contacts will be exported to. 
        Returns:
            str: The name of the file the contacts were exported to. 
        Side Effects:
            Creates a file with the name of the filename parameter from the user, and writes the contact information of all the contacts inside the AddressBook to the file.
            Each contact's information will be written on a new line in the file.
            If there aren't any contacts inside the AddressBook, a ValueError will be raised.
        """
        if not self.contacts:
            raise ValueError("There are no contacts in the AddressBook to export")
        
        with open(filename, 'w', encoding = "utf-8") as file:
            for contact in self.contacts:
                file.write(contact.get_info() + "\n")
        return filename
    

    def local_save(self, filename= "My_Local_Contacts.json"):
        """Saves all contacts the user created to a local JSON file. This allows the user to exit the program and run it again with all their contacts saved.
        Args:
            filename (str): The file name that the contacts are saved to.
        Returns:
            None
        Side Effects:
            Writes the JSON file with the current list of contacts. 
        """
        data = []
        for contact in self.contacts:
            data.append({"name": contact.name, "phone_number": contact.phone_number, "email": contact.email})

        with open(filename, "w") as file:
            json.dump(data, file)
    

    def load_local_contacts(self,filename="My_Local_Contacts.json"):
        """Loads the contacts from the local JSON file into the addressbook. 
        Args:
            filename (str): The file that the contacts are saved to.
        Returns:
            None
        Side Effects:
            Reads the JSON file with current list of contacts and appends it to the contacts. If file is not found, just returns an empty list.
        """
        try:
            with open(filename, "r") as file:
                contacts_info = json.load(file)

            self.contacts = []

            for info in contacts_info:
                contact = Contact(info ["name"], info ["phone_number"], info ["email"])
                self.contacts.append(contact)
        except FileNotFoundError:
            self.contacts = []
    
def contact_manager():
    """ This method will run the contact manager program and will show the user a menu of options they can choose from to manage their contacts.
    They can choose to add a contact, edit a contact, remove a contact, display all contacts, export contacts to a file, or quit the program. 
    Args:
        None
    Returns:
        None
    Side Effects:
        Runs the contact manager program and allows the user to manage their contacts by adding, editing, removing, displaying, and exporting contacts.
    """
    user_name = input ("Welcome to your Contact Manager! Please enter your name: ")
    user = User(user_name)
    address_book = AddressBook()
    address_book.load_local_contacts()
    print( f"\nHello {user.name}, What would you like to do?")

    while True:
        print("\n--- Menu ---")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Edit Contact")
        print("4. Remove Contact")
        print("5. Export Contact")
        print("6. Quit")
        
        choice = input("Choose an option from the menu above (1-6): ")
        if choice == "1":
            try:
                name = input("Enter Contact Name: ")
                phone_number = input("Enter Phone Number: ")
                email = input("Enter Contact Email: ")

                contact = Contact(name, phone_number, email)
                address_book.add_contact(contact)
                print("Contact has been added")
            except ValueError as error:
                print(error)

        elif choice == "2":
            if not address_book.contacts:
                print("No contacts to display")
            else:
                print("\nContacts:")
                for contact in address_book.contacts:
                    print(contact.get_info())
        elif choice == "3":
            try:
                name = input("Enter the name of contact you wish to edit: ")
                new_name = input("Enter new name, or press enter key to keep current name: ")
                new_phone_number = input("Enter new phone number, or press the enter key to keep current phone number: ")
                new_email = input("Enter new email, or press enter key to keep current email: ")

                if new_name == "":
                    new_name = None
                if new_phone_number == "":
                    new_phone_number = None
                if new_email == "":
                    new_email = None
            
                address_book.edit_contact(name, new_name, new_phone_number, new_email)
                print("Contact updated successfully.")
            except ValueError as error:
                print (error)
        
        elif choice == "4":
            try:
                name = input("Enter the name of the contact you want to remove: ")

                address_book.remove_contact(name)
                print("Contact removed successfully.")
            except ValueError as error:
                print(error)

        elif choice == "5":
            try:
                filename = input("Enter the file name that you want to export contacts to: ")

                address_book.export_contacts(filename)
                print(f"Contacts exported to {filename}!")
            except ValueError as error:
                print (error)

        elif choice == "6":
            print("You have wished to exit the program. Goodbye !")
            break
        else:
            print("Invalid choice... please choose a valid option from the menu.") 



if __name__ == "__main__":
    contact_manager()
    
