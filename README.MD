# Menu Item Assigning Assessment

This is an assessment repo that contains a solution that takes 2 files as an input, *users.txt* and *menuitems.txt*, assigns menu items and produces a JSON object

### users.txt
```
User1 NYNYN NNNNY
UserBob NNYNN NNNYY
User3 YNNYN YNNYY
User4 YYYYY YYYYY
```

### menuitems.txt
```
1, Applications Menu
2, Security Permissions Menu
3, Customers Menu
4, Accounts Menu
6, Settings Menu
5, Pricing Menu
7, Orders Menu
8, Jobs Menu
9, Profile Menu
10, Help Menu
```

### output.json
``` json
{
  "users": [
    {
      "userName": "User1",
      "menuItems": [
        "Security Permissions Menu",
        "Accounts Menu",
        "Help Menu"
      ]
    },
    {
      "userName": "UserBob",
      "menuItems": [
        "Customers Menu",
        "Profile Menu",
        "Help Menu"
      ]
    },
    {
      "userName": "User3",
      "menuItems": [
        "Applications Menu",
        "Accounts Menu",
        "Settings Menu",
        "Profile Menu",
        "Help Menu"        
      ]
    },
    {
      "userName": "User4",
      "menuItems": [
        "Applications Menu",
        "Security Permissions Menu",
        "Customers Menu",
        "Accounts Menu",
        "Pricing Menu",
        "Settings Menu",
        "Orders Menu",
        "Jobs Menu",
        "Profile Menu",
        "Help Menu"
      ]
    }
  ]
}
```

## Development Details
| IDE | Language | Version | OS 
|-----|----------|---------|-----
|Pycharm |Python |  3.10   |Windows 10

## Getting Started

There are 2 ways of running the program, through pycharm IDE or through the terminal. Which ever way you use, please remember to add python to your **path** variable

### Pycharm

1. Open the repo with Pycharm
2. Click on the configuration dropdown and click *edit configuration*![config-dropdown](/DocumentationImages/config-dropdown.png)

3. Click the *+* sign on the top to add a new configuration, give it a name and add *users.txt menus.txt* in the *parameters:* textbox ![config-window](/DocumentationImages/edit-config.png)

4. Click *apply* and *OK*
5. Add the following line of code (this is commented on the actual script, you can just uncomment it)
``` python
os.chdir(os.path.dirname(sys.argv[0]))  # Sets the runtime directory to the scripts working directory
```
6. Click the run button and voila! **NB: Input files must be in the same directory as the script**

### Terminal

1. Open terminal from the directory of the script - *assignusers.py* (If you have not installed python you can install it from here - [Install Python](https://www.python.org/downloads/release/python-3100/)). The windows installer with the version I used is also included in this repo
2. Enter the following command 
```
python assignusers.py users.txt menus.txt > output.json
```
OR
```
python assignusers.py users.txt menus.txt
```
The output will be printed onto terminal if it is not redirected