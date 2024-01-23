from file_operations import FileOperations
from utils import Utils

class Menu:
    def __init__(self):
        self.text = ""
        self.file_operations = FileOperations()
    
    def run(self):
        while True:
            print("1. New")
            print("2. Open")
            print("3. Save")
            print("4. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                self.new_note()
            elif choice == "2":
                self.open_note()
            elif choice == "3":
                self.save_note()
            elif choice == "4":
                if self.text != "":
                    confirm = input("Do you want to save before exiting? (Y/N): ")
                    if confirm.lower() == "y":
                        self.save_note()
                break
    
    def new_note(self):
        self.text = ""
        print("New note created.")
    
    def open_note(self):
        filename = input("Enter the filename: ")
        self.text = self.file_operations.load_file(filename)
        print("Note loaded.")
    
    def save_note(self):
        filename = input("Enter the filename: ")
        self.file_operations.save_file(filename, self.text)
        print("Note saved.")
    
    def word_count(self):
        count = Utils.word_count(self.text)
        print(f"Word count: {count}")
