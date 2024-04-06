import sys

if len(sys.argv) != 3:
    exit("Invalid number of arguments supplied. Usage: python assignusers.py users.txt menuitems.txt > output.json")

users_file = sys.argv[1]
menus_file = sys.argv[2]