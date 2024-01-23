class FileOperations:
    def load_file(self, filename):
        try:
            with open(filename, "r") as file:
                return file.read()
        except FileNotFoundError:
            print("File not found.")
            return ""
    
    def save_file(self, filename, text):
        try:
            with open(filename, "w") as file:
                file.write(text)
                print("File saved successfully.")
        except:
            print("Error occurred while saving the file.")
