import os

# Function to replace instances in the file
def replace_instances(file_path, search_pattern, replace_value):
    with open(file_path, 'r') as f:
        content = f.read()

    modified_content = content.replace(search_pattern, replace_value)

    with open(file_path, 'w') as f:
        f.write(modified_content)

    print(f"Replaced instances of '{search_pattern}' with '{replace_value}' in {file_path}")

# Specify the file path of apillarb.js
file_path = '/path/to/apillarb.js'

# Define the three lists: auto parts, manufacturers, and models
auto_parts = ['part1', 'part2', 'part3']  # Add your auto parts to this list
manufacturers = ['manufacturer1', 'manufacturer2', 'manufacturer3']  # Add your manufacturers to this list
models = ['model1', 'model2', 'model3']  # Add your models to this list

# Read the user input to determine which list to process
user_input = input("Enter a number (1-3) to select a list: ")

if user_input == '1':
    # Loop over the auto parts list
    for part in auto_parts:
        # Perform modifications specific to auto parts
        # Replace instances or create variables in the "apillarb.js" file
        replace_instances(file_path, 'SEARCH_PATTERN_1', part)
        replace_instances(file_path, 'SEARCH_PATTERN_2', part.upper())
        # ...

elif user_input == '2':
    # Loop over the manufacturers list
    for manufacturer in manufacturers:
        # Perform modifications specific to manufacturers
        # Replace instances or create variables in the "apillarb.js" file
        replace_instances(file_path, 'SEARCH_PATTERN_3', manufacturer)
        replace_instances(file_path, 'SEARCH_PATTERN_4', manufacturer.lower())
        # ...

elif user_input == '3':
    # Loop over the models list
    for model in models:
        # Perform modifications specific to models
        # Replace instances or create variables in the "apillarb.js" file
        replace_instances(file_path, 'SEARCH_PATTERN_5', model)
        replace_instances(file_path, 'SEARCH_PATTERN_6', model.capitalize())
        # ...

else:
    print("Invalid input! Please enter a number (1-3).")

# Print the modified code
with open(file_path, 'r') as f:
    modified_code = f.read()

print(modified_code)
