# WARNING: This code is for educational purposes only.
# It is not intended for use in real-life situations, especially for personal or business use.
# If you choose to use this code in any way, any consequences or harm that may result are your own responsibility.
# The author of this code does not assume any liability for its use in real-life scenarios.

import os
import sys
import csv
from tabulate import tabulate
#Directory Where all passwords are saved and created if it's not there
directory = 'PasswordCSV'
path = os.path.join(os.getcwd(), directory)
# Use os.mkdir() to create the folder
try:
    os.mkdir(path)
    print(f"Folder '{directory}' created successfully.")
except FileExistsError:
    pass
except Exception as e:
    print(f"An error occurred: {e}")

def main():
    # Define a table containing options for the user to choose from
    vault_list_table = [["Add new List", 1], ["View Available List", 2]]
    # Print the table using tabulate for user interaction
    # This displays a menu with two options: "Add new List" and "View Available List"
    # along with corresponding input choices (1 and 2)
    print(
        tabulate(
            vault_list_table,
            headers=["Available Option", "Input to choose"],
            tablefmt="rounded_grid",
        ),
        "\n",
    )
    # Start an indefinite loop for user input
    while True:
        try:
            # Prompt the user to enter a choice
            user_choice = int(input("Input to choose: "))
            # Check if the user's choice is not 1 or 2
            if user_choice not in [1, 2]:
                # Raise a ValueError with a message if the choice is invalid
                raise ValueError("Invalid choice. Please enter 1 or 2.")
            # Exit the loop if the input is valid
            break  
        # Catch any ValueError that may occur due to invalid input
        except ValueError as e:
            # Print an error message
            print(f"Error: {e}")

    if user_choice == 1:
        print("New Vault Creation")
        # Prompt the user to input a name for the new vault
        name = input("Input a name for the new Vault: ")
        new_vault(name)

    elif user_choice == 2:
        # Define a list of available options for the user, each option represented as a sublist
        available_options = [
            ["View all saved password in the list", 1],
            ["Add new password to the list", 2],
            ["Update password from the list", 3],
            ["Remove password from the list", 4],
        ]
        # Print a table displaying the available options and their corresponding input choices
        # The table includes two columns: "Available Option" and "Input to choose"
        # It uses the tabulate library to format the table as a grid
        print(
            tabulate(
                available_options,
                headers=["Available Option", "Input to choose"],
                tablefmt="rounded_grid",
            )
        )
        # Start an indefinite loop for user input
        while True:
            try:
                # Prompt the user to enter a choice
                available_vault_user_option = int(input("Input to choose: "))
                # Check if the user's choice is not within the valid range [1, 2, 3, 4]
                if available_vault_user_option not in [1, 2, 3, 4]:
                    # Raise a ValueError with a message if the choice is invalid
                    raise ValueError("Invalid choice. Please enter 1-4.")
                # Exit the loop if the input is valid
                break
            # Catch any ValueError that may occur due to invalid input
            except ValueError as e:
                # Print an error message
                print(f"Error: {e}")

        file_name = view_saved_csv()

        if available_vault_user_option == 1:
            # If the user chooses option 1 (View all saved passwords), call the function to print passwords table
            data = []
            with open(f'{directory}/{file_name}') as file:
                reader = csv.DictReader(file)
                for items in reader:
                    data.append(items)
            # Check if there is no data to update and Exit with a message if that's the case
            if not data:
                sys.exit("Nothing to Show, please add some Passwords to the list")
            else:
                # Display the passwords table and handle errors while updating
                print_passwords_table(file_name)

        elif available_vault_user_option == 2:
            # Get user input for Website name and Password
            website_name = input('Enter a Website Name: ')
            password = input('Enter a Password: ')
            # Add them to the choosen vault
            add_new_password(website_name, password, file_name)
        
        elif available_vault_user_option == 3:
            # If the user chooses option 3 (Update password), initialize a list to store data and read data from the file
            data = []
            with open(f'{directory}/{file_name}') as file:
                reader = csv.DictReader(file)
                for items in reader:
                    data.append(items)
            # Check if there is no data to update and Exit with a message if that's the case
            if not data:
                sys.exit("Nothing to Update, please add some Passwords to the list")
            else:
                # Display the passwords table and handle errors while updating
                print_passwords_table(file_name)
                # Error Handling
                while True:
                    try:
                        # Ask the user for the row number to update
                        num = int(input("Input a row to Update: "))
                        # Prompt the user for the updated password
                        new_password = input("Enter the updated password: ")
                        update_password(num, file_name, new_password)
                    except ValueError:
                        print('Invalid Input, Please correct your input')
                    else:
                        break

        elif available_vault_user_option == 4:
            # If the user chooses option 4 (Remove password), initialize a list to store data and read data from the file
            data = []
            with open(f'{directory}/{file_name}') as file:
                reader = csv.DictReader(file)
                for items in reader:
                    data.append(items)
            # Check if there is no data to remove and Exit with a message if that's the case
            if not data:
                sys.exit("Nothing to Remove, please add some Passwords to the list")
            else:
                # Display the passwords table and handle errors while removing
                print_passwords_table(file_name)
                # Error Handle If the user input other than int
                while True:
                    try:
                        # Ask the user for the row number to delete
                        remove_password(int(input("Input a row to delete: ")), file_name)
                    except ValueError:
                        print('Invalid Input, Please correct your input')
                    else:
                        break

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
            elif choice == "Y":
                pass
                name = input("Input a name for the new Vault: ")
        else:
            # If the file was created successfully or if it didn't exist, exit the loop
            break

def view_saved_csv():
    # Initialize an empty dictionary to store available CSV files and their associated numbers.
    available_csv_dict = {}
    # Initialize a counter variable.
    n = 0
    # Get the current directory path.
    current_dir = os.path.join(os.getcwd(), directory)
    # Check if there is anyfile in the directory
    contents = os.listdir(current_dir)
    if len(contents) == 0:
        # If nothing in there Exit
        sys.exit("No Vault found, please create a new one")
    # Walk through the directory tree and list all files.
    for root, dirs, files in os.walk(current_dir):
        for file in files:
            n += 1  # Increment the counter for each file found.
            # Split the file name into its name and extension.
            file_name, file_ext = os.path.splitext(file)
            # If the extension is .csv, add the file name and its associated number to the dictionary.
            if file_ext == ".csv":
                available_csv_dict[file_name + file_ext] = n
    # Convert the dictionary into a list of lists (key-value pairs).
    table_data = [[key, value] for key, value in available_csv_dict.items()]
    # Print a table with all the available vault name as csv file
    print(
        tabulate(
            table_data,
            headers=["Available Lists", "Input to choose"],
            tablefmt="rounded_grid",
        )
    )
    while True:
        # Getting user input to choose from the table of csv file
        try:
            view_available_password_input = int(
                input("Input to choose a vault: ")
            )
        except ValueError:
            print("Invalid Input")
        else:
            for items in table_data:
                # Checking if the user Input is available from the input to choose
                if items[1] == view_available_password_input:
                    # Return the file name with the extension
                    return items[0]
            else:
                # Print `Invalid input` if the user gave an input outside the table
                print("Invalid input")
                pass

def add_new_password(website_name, password, file_name):
    if not password:
        print("No password was typed")
        return False
    if is_duplicate(website_name, password, file_name):
        print("Data already Exist")
        return False
    else:
        # Create a list containing a dictionary with the website name and password
        add_data = [{"Website Name": website_name, "Passwords": password}]
        # Open the CSV file for appending ('a' mode) and create a CSV writer object
        # The 'newline' parameter ensures proper line endings in the CSV file
        with open(f'{directory}/{file_name}', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Website Name', 'Passwords'])
            # Write the data in the 'add_data' list to the CSV file
            writer.writerows(add_data)
        return True

def remove_password(num, file_name):
    # Create an empty list to store the data after removing a row
    remove_data = []
    # Open the CSV file for reading
    with open(f'{directory}/{file_name}', 'r', newline='') as file:
        # Create a CSV reader object
        reader = csv.DictReader(file)
        # Iterate through each row in the CSV file and append it to remove_data
        for items in reader:
            remove_data.append(items)
    # Check if the row number is valid (within the range of the data)
    if 1 <= num <= len(remove_data):
        # Delete the specified row
        del remove_data[num - 1]
        # Open the CSV file for writing
        with open(f'{directory}/{file_name}', 'w', newline='') as file:
            # Get the fieldnames from the first row
            fieldnames = ["Website Name", "Passwords"]
            # Create a CSV writer object
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            # Write the header row
            writer.writeheader()
            # Write the remaining data without the deleted row
            writer.writerows(remove_data)
        return True
    else:
        print("Invalid row number. No changes were made to the file.")
        return False

def update_password(num, file_name, new_password):
    # Open the CSV file for reading and initialize the update_data list
    update_data = []
    with open(f'{directory}/{file_name}', 'r', newline='') as file:
        # Create a CSV reader object
        reader = csv.DictReader(file)
        # Iterate through each row in the CSV file and append it to update_data
        for items in reader:
            update_data.append(items)
    # Check if the row number is valid
    if 1 <= num <= len(update_data):
        # Update the password in the selected row
        update_data[num - 1]["Passwords"] = new_password
        # Open the CSV file for writing
        with open(f'{directory}/{file_name}', 'w', newline='') as file:
            # Get the fieldnames from the first row
            fieldnames = ["Website Name", "Passwords"]
            # Create a CSV writer object
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            # Write the header row
            writer.writeheader()
            # Write the updated data to the CSV file
            writer.writerows(update_data)
        
        print("Password updated successfully.")
        return True
    else:
        print("Invalid row number. No changes were made to the file.")
        return False

def print_passwords_table(file_name):
    data_set = {}
    # Open the CSV file for reading
    with open(f"{directory}/{file_name}") as file:
        # Create a CSV reader
        readers = csv.reader(file)
        # Read the first row as headers and store them in a list
        headers = next(readers)
        # Initialize empty lists for each header in the data_set dictionary
        for header in headers:
            data_set[header] = []
        # Iterate through each row in the CSV file
        for row in readers:
            # Append each value to the corresponding header list in data_set
            for header, value in zip(headers, row):
                data_set[header].append(value)
    # Create a custom index list starting from 1
    custom_indices = list(range(1, len(data_set["Website Name"]) + 1))
    # Print the data_set as a tabulated table
    print(tabulate(data_set, headers=data_set, tablefmt='rounded_grid', showindex=custom_indices))

def check_password_available_in_list(file_name):
    data = []
    with open(f'{directory}/{file_name}') as file:
        reader = csv.DictReader(file)
        for items in reader:
            data.append(items)
    # Check if there is no data to update and Exit with a message if that's the case
    if not data:
        sys.exit("Nothing to Update, please add some Passwords to the list")
    else:
        # Display the passwords table and handle errors while updating
        print_passwords_table(file_name)

def is_duplicate(website_name, password, file_name):
    # Open the CSV file for reading
    with open(f"{directory}/{file_name}", 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Website Name"] == website_name and row["Passwords"] == password:
                return True  # Found a duplicate
    return False  # No duplicate found

if __name__ == "__main__":
    main()