try:
    with open("my_file.txt", "w") as file:
        file.write("I am Mwangi this is my python adventure.\n")
        file.write("I am 24.\n")
        file.write("Have fun, and good day!\n")
except PermissionError:
    print("Error: Cannot create or write to the file. Please check the file permissions.")
except IOError:
    print("Error: An I/O error occurred while creating or writing to the file.")
finally:
    print("File creation step completed.")

try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("Contents of the file:")
        print(content)
except FileNotFoundError:
    print("Error: The file 'my_file.txt' does not exist.")
except IOError:
    print("Error: An I/O error occurred while reading the file.")
finally:
    print("File reading step completed.")

try:
    with open("my_file.txt", "a") as file:
        file.write("This is the first additional line.\n")
        file.write("This is the second additional line.\n")
        file.write("This is the third additional line.\n")
except PermissionError:
    print("Error: Cannot append to the file. Please check the file permissions.")
except IOError:
    print("Error: An I/O error occurred while appending to the file.")
finally:
    print("File appending step completed.")
