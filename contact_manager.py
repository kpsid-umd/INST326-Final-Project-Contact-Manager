# This program is a contact manager that will allow users to manage their contacts
# by adding, editing, and removing contacts. Each contact will list important information
# like the contact's name, phone number, and email address.

# Group Members: Siddharth Padithaya, Rayan Shah, and Raymond Dickscheid

class User:
    """ This class stores information related to the user such as adding user info, editing user info and displaying user info. 
    Attributes:
        name (str): The name of the user
    """
    def __init__(self, name):
        """
        This method initializes the user with a name
        """
        self.name = name
        
    def display_user_info(self):
        """
        Returns the user's name, email, and phone number about the user (will be added later)

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
            name (str): The name of the contact
            phone_number (str): The phone number of the contact
            email (str): The email address of the contact
        Returns:
            str: A string with the contact's name, phone number, and email address
        Side Effects:
            None
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

        """
        for contacts in self.contacts:
            if contacts.name == contact.name:
                raise ValueError(" A contact with this name already exists. If this is a different contact, please add the last name initial to differentiate between them.")
        self.contacts.append(contact)
    
    def find_contact(self, name):
        """
        Finds a contact in the address book by name and returns the contact's information.
        Args:
            name (str): The name of the contact that needs its information found
        Returns:
            Contact: The contact with the name that was searched for. 
        Side Effects:
            If a contact with the name that was searched for is not found, a Value Error will be raised.
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
        """
        contact = self.find_contact(name)

        if new_name:
            for names in self.contacts:
                if names.name == new_name and names != contact:
                    raise ValueError(" A contact with this name already exists.")
                
        contact.update_info(new_name, new_phone_number, new_email)


    def remove_contact(self, name):
        """
        Removes a contact from the address book
        Args:
            name (str): The name of the contact that needs to be removed
        Returns:
            None
        Side Effects:
            Removes the contact information that was searched from the AddressBook. If a contact with the name that was searched is not found, a Value Error is raised. 
        """
        contact = self.find_contact(name)
        self.contacts.remove(contact)

    def export_contacts(self, filename):
        """ Exports the contacts in the address book to a file
        Args:
            filename (str): The name of the file the contacts will be exported to. 
        Returns:
            str: The name of the file the contacts were exported to and created locally in the folder of the program. 
        Side Effects:
            Creates a file with the name of the filename parameter from the user, and writes the contact information of all the contacts inside the AddressBook to the file.
            Each contact's information will be writted on a new line in the file.
            If there aren't any contacts inside the AddressBook, a ValueError will be raised.
        """
        if not self.contacts:
            raise ValueError("There are no contacts in the AddressBook to export")
        
        with open(filename, 'w', encoding = "utf-8") as file:
            for contact in self.contacts:
                file.write(contact.get_info() + "\n")
        return filename
    
def contact_manager():
    """ This method will run the contact manager program and will show the user a menu of options they can choose from to manage their contacts.
    They can choose to add a contact, edit a contact, remove a contact, display all contacts, export contacts to a file, or quit the program. 
    Args:
        None
    Returns:
        None
    Side Effects:
        Runs the contact manager program and allows the user to manage their contacts by adding, editing, removing, displaying, and exporting contacts."""
    user_name = input ("Welcome to your Contact Manager! Please enter your name: ")
    user = User(user_name)
    address_book = AddressBook()
    print(f"Hello {user.name}, What would you like to do?")
    while True:
        # Need to add the rest of the menu options and the functions for each of them. (will add later)
        
        choice = input("Choose an option from the menu above (1-6): ")
        if choice == "1":
            # call the add contact function
            pass
        elif choice == "2":
            # call the display contact function
            pass
        elif choice == "3":
            # call the edit contact function
            pass
        elif choice == "4":
            # call the remove contact function
            pass
        elif choice == "5":
            # call the export contacts function
            pass
        elif choice == "6": 
            # quit the program
            pass
        else:
            print("Invalid choice!!! Please choose a valid option from the choice menu.") 



if __name__ == "__main__":
    contact_manager()