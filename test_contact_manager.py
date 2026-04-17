import unittest
from contact_manager import User, Contact, AddressBook

class TestContactManager(unittest.TestCase):
    def test_user_name(self):
        user = User("Matthew")
        self.assertEqual(user.name, "Matthew")

    def test_display_user_info(self):
        user = User("Matthew")
        user.edit_user_name("Matt")
        self.assertEqual(user.name, "Matt")
    
    def test_new_contact(self):
        contact = Contact("Andrew", "240-223-3481", "ajohnson@terpmail.umd.edu")
        self.assertEqual(contact.name, "Andrew")
        self.assertEqual(contact.phone_number, "240-223-3481")
        self.assertEqual(contact.email, "ajohnson@terpmail.umd.edu")

    def test_update_contact_info(self):
        contact = Contact("Andrew", "240-223-3481", "ajohnson@terpmail.umd.edu")
        contact.update_info(phone_number = "301-222-3214")
        self.assertEqual(contact.phone_number, "301-222-3214")

    def test_add_contact_to_address_book(self):
        book = AddressBook()
        contact = Contact("Andrew", "240-223-3481", "ajohnson@terpmail.umd.edu")
        book.add_contact(contact)
        self.assertEqual(len(book.contacts),1)

if __name__ == "__main__":
    unittest.main()