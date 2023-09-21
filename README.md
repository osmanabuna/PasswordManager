# Password Manager
A command list Password Manager to manage all of your password using python
#### Video Demo:  <URL HERE>
### __`Warning`__:
- This program is for educational purposes only.
- It is not intended for use in real-life situations, especially for personal or business use.
- If you choose to use this program in any way, any consequences or harm that may result are your own responsibility.
- The author of this program does not assume any liability for its use in real-life scenarios.

### Installation:
Using pip to install tabulate
```
$ pip install tabulate
```
or
```
$ pip install -r requirements.txt
```
### Usage
Use python to run the application
```
$ python project.py
```
Use pytest to test the application
```
$ pytest test_project.py
```
or
```
$ python -m pytest test_project.py
```

### Description:
Password Manager kinda inspired from lastpass in which user can store password in different vault

Like the user can have two different vault for different roles for like busssines vault and personal vault

And store all of his/her personal account password in personal vault and all bussines account password in business vault

### Code Explanation:
It starts by importing necessary libraries/modules such as `os`, `sys`, `csv`, and `tabulate`.

It defines a `directory` named 'PasswordCSV' where all the password data will be saved, the variable `directory` could be changed to the user liking.
```python
directory = 'PasswordCSV'
```

If this directory doesn't exist, it attempts to create it using os.mkdir(). If the folder already exists, it simply proceeds.

```python
path = os.path.join(os.getcwd(), directory)
# Use os.mkdir() to create the folder
try:
    os.mkdir(path)
    print(f"Folder '{directory}' created successfully.")
except FileExistsError:
    pass
```
The main() function serves as the main entry point of the program. It provides a menu system for the user to perform various operations related to managing passwords stored in CSV files.

The main menu offers two options:

- "Add new List" (Option 1): This option allows the user to create a new password list (CSV file).
- "View Available List" (Option 2): This option allows the user to choose an existing password list for further actions.

- Both for the options the user should enter an int(which means number) otherwise the user be told again to re-enter

If the user selects "Add new List," In which it will run the `new_vault()` function

the program prompts the user to input a name for the new vault In the main function (CSV file). 

```python
if user_choice == 1:
    print("New Vault Creation")
    # Prompt the user to input a name for the new vault
    name = input("Input a name for the new Vault: ")
    new_vault(name)
```
The `name` in which it is a string will then be passed to `new_vault()` function so it will create the csv file using the name

```python
def new_vault(name):
    # Start a loop to create a new vault
    while True:
        # Check if the provided name does not end with ".csv"
        if not name.endswith(".csv"):
            # Append ".csv" to the name if it's missing
            name += ".csv"
        # Create the full file path by joining directory with the provided name
        file_path = os.path.join(directory, name)
        try:
            # Try to open the file in "x" mode (exclusive creation) for writing
            # This will create a new file with the specified name if it doesn't exist
            # and raise a FileExistsError if the file already exists
            with open(file_path, "x", newline="") as file:
                # Create a CSV writer object for the new file with specific fieldnames
                creator = csv.DictWriter(file, fieldnames=["Website Name", "Passwords"])
                # Write the header row to the new CSV file
                creator.writeheader()
        except FileExistsError:
            # If the file already exists, prompt the user for a choice to continue or not
            print("File already exists. Do you want to continue (Y/N): ", end="")
            choice = input().upper()
            # If the user enters "N" (no), exit the loop and don't create a new vault
            if choice == "N":
                break
        else:
            # If the file was created successfully or if it didn't exist, exit the loop
            break
```

The `if` statement checks whether the variable `name` entered by the user ends with ".csv." If it doesn't already end with ".csv," the statement automatically appends it to the `name` variable.

If a file with the same `name` already exists, it asks the user whether to continue or not, be letting the user to input `Y` or `N` whether in capital or not

If the user selects "View Available List," the program lists all existing password lists (CSV files) in the 'PasswordCSV' directory and asks the user to choose one, in which it execute the 

```python
def print_passwords_table(file_name) 
``` 
in line 320

After selecting a password list, the user is presented with a submenu containing the following options:

- "View all saved password in the list" (Option 1): Displays all the passwords stored in the selected list.
- "Add new password to the list" (Option 2): Allows the user to add a new password to the selected list.
- "Update password from the list" (Option 3): Allows the user to update an existing password in the selected list.
- "Remove password from the list" (Option 4): Allows the user to remove a password from the selected list.

Depending on the user's choice, the program calls corresponding functions to perform the selected operation, such as 

`adding` in which the function below in line 243 get executed to add new password into the list
```python
def add_new_password(website_name, password, file_name)
```

`updating` in which the function below in line 290 get executed to update password from the list

```python
def update_password(num, file_name, new_password)
```

`removing` in which the function below in line 261 get executed to remove password from the list

```python
def remove_password(num, file_name)
```

The program provides error handling for invalid user inputs and ensures that operations are only performed on valid data.

The code also includes functions like `view_saved_csv()`, `check_password_available_in_list()`, `print_passwords_table()`, and `is_duplicate()` to handle specific tasks related to managing passwords and CSV files.

## Additional Functionality

1. ### `view_saved_csv()` found in line `193`

    The `view_saved_csv()` function serves the following purposes in the code:

    1. It lists all the available password lists (CSV files) in the 'PasswordCSV' directory.
    2. It assigns a unique number to each available CSV file, allowing the user to choose a file by entering its corresponding number.
    3. It takes user input to select a password list (CSV file) by entering the number associated with it.
    4. It returns the name of the selected CSV file, which will be used for subsequent operations such as `viewing`, `adding`, `updating`, or `removing` passwords in that file.

2. ### `print_passwords_table()` found in line `320`
    The `print_passwords_table(file_name)` function in the provided code is responsible for printing a tabulated table of passwords that are stored in a selected CSV file (password list). Here's what it does:

    1. It takes a single argument `file_name`, which represents the name of the CSV file (password list) from which to retrieve and print the passwords.

    2. Inside the function, it initializes an empty dictionary called `data_set`. This dictionary will be used to organize the data read from the CSV file.

    3. It opens the specified CSV file (`file_name`) for reading.

    4. It uses the `csv.reader` to read the contents of the CSV file. The first row of the CSV file, which typically contains the headers, is stored as the `headers` variable.

    5. For each header in the `headers` list, the function initializes an empty list in the `data_set` dictionary. These lists will be used to store the values (passwords) associated with each header.

    6. The function then iterates through the rows of data in the CSV file, appending the values in each row to their respective lists in the `data_set` dictionary.

    7. It creates a custom index list starting from 1 to represent the row numbers in the table.

    8. Finally, it uses the `tabulate` library to print the `data_set` as a tabulated table. The `headers` are used as column headers, and the `data_set` stores the rows of data. The custom indices are shown on the left to represent row numbers.

3. ### `check_password_available_in_list()` found in line `341`

    So, `check_password_available_in_list(file_name)` provides an extra level of validation to ensure that there is data to display, whereas `print_passwords_table(file_name)` simply prints the table, even if it's empty.

    This function also prints the tabulated table of passwords, but it includes additional logic to check whether there are passwords in the file. If there are no passwords in the file, it displays an error message and exits.

    Here's the functionality of `check_password_available_in_list(file_name)`:

    1. It opens the specified CSV file (password list) for reading.

    2. It reads the data from the CSV file and stores it in a dictionary called data_set. This dictionary is structured such that each header from the CSV file becomes a key, and the corresponding rows of data become values in lists associated with those keys.

    3. It prints the data in data_set as a tabulated table using the tabulate library.

    4. It provides an error message and exits if there is no data to display in the CSV file.

4. ### `is_duplicate()` found in line `354`
    The `is_duplicate(website_name, password, file_name)` function is used to check whether a given combination of a website name and password already exists in a specified CSV file (password list). Here's what it does:

    1. It takes three arguments:

        1. `website_name`: The name of the website for which the duplication is checked.
        2. `password`: The password associated with the website name.
        3. `file_name`: The name of the CSV file (password list) in which the duplication is checked.
    
    2. Inside the function, it opens the specified CSV file (`file_name`) for reading.

    3. It uses the `csv.DictReader` to read the contents of the CSV file row by row.

    4. It iterates through each row in the CSV file and compares the `website_name` and `password` with the values in each row.

    5. If it finds a row where both the `website_name` and `password` match the provided values, it returns `True`, indicating that a duplicate entry exists.

    6. If no such matching row is found in the CSV file, it returns `False`, indicating that there is no duplicate entry for the given website name and password.

    The primary purpose of `is_duplicate()` is to prevent the addition of duplicate entries in the password list. Before adding a new password, it checks whether a combination of the website name and password already exists in the specified CSV file. If a duplicate is detected, it returns `True`, and the program can then handle the duplicate accordingly (e.g., display an error message to the user and prevent the addition of the duplicate entry).

The `main()` function is called at the end of the code when it's executed, starting the main menu and user interaction.

Overall, this code serves as a basic command-line password manager that allows users to create and manage multiple password lists (vaults) stored in CSV files. Users can add, update, and remove passwords within these lists.