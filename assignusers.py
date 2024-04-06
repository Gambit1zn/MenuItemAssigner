import sys
import os

if len(sys.argv) != 3:
    exit("Invalid number of arguments supplied. Usage: python assignusers.py users.txt menuitems.txt > output.json")

os.chdir(os.path.dirname(sys.argv[0]))

users_file = sys.argv[1]
menus_file = sys.argv[2]

try:
    with open(users_file, 'r') as user_file:
        users = user_file.readlines()


except FileNotFoundError:
    print("User file not found. Please ensure files are in the same directory as the script and the name is correct")

# User consumption and validation
user_objects = {}

for user in users:
    partitions = user.replace("\n", "").split(" ")

    increment = 0
    user_options = []
    for partition in partitions:
        increment = increment + 1
        if increment == 1:  # the first partition will always be the username
            username = partition
        else:
            for option in partition:
                if option in ['Y', 'N']:
                    user_options.append(option)
                else:
                    exit(f"Invalid option found in users.txt for user: {username}. Options must be 'Y' or 'N'.")

            user_objects[username] = user_options

print(user_objects)
