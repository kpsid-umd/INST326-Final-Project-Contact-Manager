import unittest
from contact_manager import User, Contact, AddressBook

class TestContactManager(unittest.TestCase):
    def test_user_name(self):
        user = User("Matthew")
        self.assertEqual(user.name, "Matthew")

    def test_edit_user_name(self):
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
    
    def test_add_duplicate_contact_to_address_book(self):
        book = AddressBook()
        contact1 = Contact("James", "240-223-2133", "ilovecars@gmail.com")
        contact2 = Contact("James", "240-223-2133", "ilovecars@gmail.com")

        book.add_contact(contact1)
        with self.assertRaises(ValueError):
            book.add_contact(contact2)

    def test_find_contact_found(self):
        book = AddressBook()
        contact = Contact("Alex", "301-234-2853", "alex@gmail.com")
        book.add_contact(contact)

        self.assertEqual(book.find_contact("Alex"), contact)

    def test_find_contact_not_found(self):
        book = AddressBook()
        with self.assertRaises(ValueError):
            book.find_contact("Could not be found")
    
    def test_edit_contact_info(self):
        book = AddressBook()
        contact = Contact("Sid", "223-234-7535", "sid01@gmail.com")
        book.add_contact(contact)

        book.edit_contact("Sid", new_phone_number = "230-394-5654")
        self.assertEqual(contact.phone_number, "230-394-5654")
    
    def test_edit_contact_info_duplicate_name(self):
        book = AddressBook()
        contact1 = Contact("Ray", "674-248-2484", "ray012@gmail.com")
        contact2 = Contact("Jay", "303-267-2739", "jayiscool@gmail.com")

        book.add_contact(contact1)
        book.add_contact(contact2)

        with self.assertRaises(ValueError):
            book.edit_contact("Ray", new_name = "Jay")
    
    def test_remove_contact_found(self):
        book = AddressBook()
        contact = Contact("Jack", "240-223-3481", "ja1@gmail.com")

        book.add_contact(contact)
        book.remove_contact("Jack")
        self.assertEqual(len(book.contacts), 0)
    
    def test_remove_contact_not_found(self):
        book = AddressBook()
        with self.assertRaises(ValueError):
            book.remove_contact("Contact could not be found")
    
    def test_export_contacts(self):
        book = AddressBook()
        contact = Contact("Emily", "940-334-4579", "emil@gmail.com")
        book.add_contact(contact)

        file_name = "My Contacts.txt"
        book.export_contacts(file_name)

        with open(file_name, "r") as file:
            self.assertIn("Emily", file.read())

    def test_export_contacts_empty(self):
        book = AddressBook()
        
        with self.assertRaises(ValueError):
            book.export_contacts("Empty.txt")
    
    def test_get_contact_info(self):
        contact = Contact("Micheal", "459-344-4931", "m21@yahoo.com")
        info = contact.get_info()

        self.assertIn("Micheal", info)
        self.assertIn("459-344-4931", info)
        self.assertIn("m21@yahoo.com", info)
    
    def test_missing_values_contact_info(self):
        with self.assertRaises(TypeError):
            Contact("Jason", "345-344-8595")

    
    def test_multiple_contact_fields(self):
        contact = Contact("Sarah", "240-223-3481", "sarah1@gmail.com")
        contact.update_info(name = "Sarah J", email = "Saraj1@gmail.com")

        self.assertEqual(contact.name, "Sarah J")
        self.assertEqual(contact.email, "Saraj1@gmail.com")
        self.assertEqual(contact.phone_number, "240-223-3481")
        
if __name__ == "__main__":
    unittest.main()