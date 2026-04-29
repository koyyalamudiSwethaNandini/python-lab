import re

# Function to check if string starts and ends with same character
def check_start_end_same_char(s):

    # Regular expression pattern
    pattern = r'^[a-z]$|^([a-z]).*\1$'

    # Apply search function
    if re.search(pattern, s):
        return True
    else:
        return False


# Input string
s = input("Enter a string: ")

if check_start_end_same_char(s):
    print("String starts and ends with same character")
else:
    print("String does not start and end with same character")
