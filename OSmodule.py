#Use the OS module to perform
#1. Create a directory
#2. Directory Listing
#3. Search for “.py” files
#4. Remove a particular file

import os

def create_directory(directory_name):
    """Create a directory with the given name."""
    try:
        os.makedirs(directory_name, exist_ok=True)
        print(f"Directory '{directory_name}' created successfully.")
    except Exception as e:
        print(f"Error creating directory '{directory_name}': {e}")

def list_directory(directory_name):
    """List the contents of the given directory."""
    try:
        contents = os.listdir(directory_name)
        print(f"Contents of '{directory_name}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"Directory '{directory_name}' does not exist.")
    except Exception as e:
        print(f"Error listing directory '{directory_name}': {e}")

def search_py_files(directory_name):
    """Search for '.py' files in the given directory."""
    try:
        py_files = [f for f in os.listdir(directory_name) if f.endswith('.py')]
        print(f"'.py' files in '{directory_name}':")
        for py_file in py_files:
            print(py_file)
    except FileNotFoundError:
        print(f"Directory '{directory_name}' does not exist.")
    except Exception as e:
        print(f"Error searching for '.py' files in '{directory_name}': {e}")

def remove_file(file_path):
    """Remove the specified file."""
    try:
        os.remove(file_path)
        print(f"File '{file_path}' removed successfully.")
    except FileNotFoundError:
        print(f"File '{file_path}' does not exist.")
    except Exception as e:
        print(f"Error removing file '{file_path}': {e}")

def main():
    while True:
        print("\nMenu:")
        print("1. Create a directory")
        print("2. List the contents of a directory")
        print("3. Search for '.py' files in a directory")
        print("4. Remove a particular file")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            directory_name = input("Enter the directory name to create: ")
            create_directory(directory_name)
        elif choice == "2":
            directory_name = input("Enter the directory name to list: ")
            list_directory(directory_name)
        elif choice == "3":
            directory_name = input("Enter the directory name to search for '.py' files: ")
            search_py_files(directory_name)
        elif choice == "4":
            file_path = input("Enter the file path to remove: ")
            remove_file(file_path)
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-5).")

if __name__ == "__main__":
    main()
