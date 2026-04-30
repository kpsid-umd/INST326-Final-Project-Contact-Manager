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

        self.assertEqual(book.find_contact("Alex"), contact())

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
            

    

        

if __name__ == "__main__":
    unittest.main()