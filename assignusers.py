import sys
import os
import json

if len(sys.argv) != 3:
    exit("Invalid number of arguments supplied. Usage: python assignusers.py users.txt menuitems.txt > output.json")

# os.chdir(os.path.dirname(sys.argv[0]))  # Sets the runtime directory to the scripts working directory
# (this was looking in the bin folder), ONLY NEEDED WHEN RUNNING THIS FROM PYCHARM VIRTUAL ENVIRONMENT

users_file = sys.argv[1]
menus_file = sys.argv[2]

try:
    with open(users_file, 'r') as user_file:
        users = user_file.readlines()

except FileNotFoundError:
    sys.stderr.write("User file not found. Please ensure files are in the same directory as the script and the name "
                     "is correct")

# User consumption and validation
user_objects = {}
username_keys = []

for user in users:
    partitions = user.replace("\n", "").split(" ")

    user_increment = 0
    user_options = []
    for partition in partitions:
        user_increment = user_increment + 1
        if user_increment == 1:  # the first partition will always be the username
            username = partition
            username_keys.append(username)  # used later for mapping
        else:
            for option in partition:
                if option in ['Y', 'N']:
                    user_options.append(option)
                else:
                    exit(f"Invalid option found in users.txt for user: {username}. Options must be 'Y' or 'N'.")

            user_objects[username] = user_options

# Menu consumption and validation
menu_objects = {}

try:
    with open(menus_file, 'r') as menu_file:
        menu_items = menu_file.readlines()

except FileNotFoundError:
    sys.stderr.write("Menu file not found. Please ensure files are in the same directory as the script and the name "
                     "is correct")

for menu_item in menu_items:
    menu_item_partition = menu_item.split(',')

    if menu_item_partition[0].isdigit():
        menu_item_position = int(menu_item_partition[0])
    else:
        exit(f"Data invalid for file: {menus_file}, item: {menu_item_partition[len(menu_item_partition) - 1]}. Menu "
             f"item must have a number separated by comma and then its item name, eg: 1, menuItem")

    menu_item_value = menu_item_partition[len(menu_item_partition) - 1].replace('\n', "").strip()
    menu_objects[menu_item_position] = menu_item_value

#  Mapping users to menu items

root_object = {}
users = []

for key in username_keys:
    options = user_objects[key]
    option_number = 0
    user_menu_items = []

    for user_option in options:
        option_number = option_number + 1
        if user_option == 'Y':
            user_menu_items.append(menu_objects[option_number])

    user = {
        "username": key,
        "menuItems": user_menu_items
    }
    users.append(user)

root_object["users"] = users
json_data = json.dumps(root_object)

# Write to output file
sys.stdout.write(json_data)

