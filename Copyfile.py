#Write a Python program to copy the contents of a file into another file, line by line.

def copy_file(source_file, destination_file):
    try:
        # Open source file in read mode
        with open(source_file, 'r') as src:
            # Open destination file in write mode
            with open(destination_file, 'w') as dest:
                # Read each line from source file and write to destination file
                for line in src:
                    dest.write(line)
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print("One of the files does not exist.")
    except IOError as e:
        print(f"Error occurred while copying the file: {e}")

def main():
    source_file = input("Enter the source file name: ")
    destination_file = input("Enter the destination file name: ")

    copy_file(source_file, destination_file)

if __name__ == "__main__":
    main()
