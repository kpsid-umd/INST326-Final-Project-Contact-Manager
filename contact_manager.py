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
    def __init__(self, name, phone_number, email):
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

    """
    def __init__(self):
        """
        Initializes the address book with an empty list of blank contacts.
        """
        self.contacts = []

    def add_contact(self, contact):
        """
        Adds a contact to the address book.
        """
        self.contacts.append(contact)
        
    def edit_contact(self, contact):
        """
        Edits a contact's information in the address book (will be added later)
        """
        pass
    def remove_contact(self, contact):
        """
        Removes a contact from the address book (Will be added later)
        """
        pass