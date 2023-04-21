import sys
import time

phonebook = {
    "contact":"08034262725",
    "contact_name":"Eniola",
    "email_address":"heniola395@gmail.com"
}

class Phonebook:
    def __init__(self):
        self.welcome_message = "Hello there, Welcome to the phonebook program"
        self.about = "Here you can save your beloved's contact with their name and email address after which you can search for their contact with their name"
        self.menu()
        
    def menu(self):
        print(self.welcome_message)
        time.sleep(1)
        print(self.about)
        
        
phonebookProgram = PhoneBook()