import sys
import os

if len(sys.argv) != 3:
    exit("Invalid number of arguments supplied. Usage: python assignusers.py users.txt menuitems.txt > output.json")

os.chdir(os.path.dirname(sys.argv[0]))  # Sets the runtime directory to the scripts working directory, for some reason
# this was looking in the bin folder

users_file = sys.argv[1]
menus_file = sys.argv[2]

try:
    with open(users_file, 'r') as user_file:
        users = user_file.readlines()


except FileNotFoundError:
    print("User file not found. Please ensure files are in the same directory as the script and the name is correct")

# User consumption and validation
print("Consuming and validating files...")
user_objects = {}

for user in users:
    partitions = user.replace("\n", "").split(" ")

    user_increment = 0
    user_options = []
    for partition in partitions:
        user_increment = user_increment + 1
        if user_increment == 1:  # the first partition will always be the username
            username = partition
        else:
            for option in partition:
                if option in ['Y', 'N']:
                    user_options.append(option)
                else:
                    exit(f"Invalid option found in users.txt for user: {username}. Options must be 'Y' or 'N'.")

            user_objects[username] = user_options

print(f"data in {users_file} validated and consumed successfully!")

# Menu consumption and validation
menu_objects = {}

try:
    with open(menus_file, 'r') as menu_file:
        menu_items = menu_file.readlines()

except FileNotFoundError:
    print("Menu file not found. Please ensure files are in the same directory as the script and the name is correct")

for menu_item in menu_items:
    menu_item_partition = menu_item.split(',')

    if menu_item_partition[0].isdigit():
        menu_item_position = int(menu_item_partition[0])
    else:
        exit(f"Data invalid for file: {menus_file}, item: {menu_item_partition[len(menu_item_partition) - 1]}. Menu "
             f"item must have a number separated by comma and then its item name, eg: 1, menuItem")

    menu_item_value = menu_item_partition[len(menu_item_partition) - 1].replace('\n', "").strip()
    menu_objects[menu_item_position] = menu_item_value

print(f"data in {menus_file} validated and consumed successfully!")
print("Mapping and constructing object...")

