# File Creation
try:
    # Creating a new text file named "my_file.txt" in write mode ('w')
    with open("my_file.txt", "w") as file:
        # Writing at least three lines of text to the file
        file.write("This is line 1\n")
        file.write("12345\n")
        file.write("Line 3: End of file creation\n")

except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")

# File Reading and Display
try:
    # Opening "my_file.txt" in read mode ('r')
    with open("my_file.txt", "r") as file:
        # Reading the contents of "my_file.txt"
        file_contents = file.read()
        # Displaying the contents on the console
        print("Contents of my_file.txt:")
        print(file_contents)

except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")

# File Appending
try:
    # Opening "my_file.txt" in append mode ('a')
    with open("my_file.txt", "a") as file:
        # Appending three additional lines of text to the existing content
        file.write("\nAppending line 4\n")
        file.write("Line 5: Append mode\n")
        file.write("Line 6: End of file appending\n")

except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")

# Error Handling using try, except, and finally blocks
try:
    # Opening "my_file.txt" in read mode ('r')
    with open("my_file.txt", "r") as file:
        # Reading the contents of "my_file.txt"
        file_contents = file.read()
        # Displaying the contents on the console
        print("\nContents of my_file.txt after appending:")
        print(file_contents)

except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")

finally:
    print("\nEnd of file handling operations.")
