import os
import re

# This block opens the file specified by filename and reads its contents into the data variable as a list of lines.
# It also prints the first 10 lines of the file for debugging purposes.

# Define the name of the file and folder to be used
filename = 'apillarb.js'

# Open and read the content of apillarb.js
with open(filename, 'r') as f:
    data = f.readlines()

# Debug - Print the first 10 lines of the file
print(data[:10])

# This block opens the file named part-names.js and reads its contents into the auto_part_data variable. 
# It uses regular expressions to find all auto part names in the auto_part_data string and stores them in 
# the auto_parts list. The list comprehension filters out any empty matches.

with open('part-names.js') as f:
    auto_part_data = f.read()

    # Find all auto part names using regular expression
    auto_part_matches = re.findall(r"partname:(?:\s*)'(.+?)'", auto_part_data)
    
    # Debug - Print the matches
    print(auto_part_matches)

    # Use re.findall() to obtain all matches and filter out any empty matches
    # This ensures that the auto part names are preserved in the order they appear in the part-names.js file
    auto_parts = [match for match in auto_part_matches if match]

    # Debug - Print the first 10 auto part names
    print(auto_parts[:10])

    # Should Print Out This List, Check For Accuray, Change The Range :10 to :100 If You Need To Check More
    ['Air Box or Air Cleaner', 'Air Condition Vents or Heater Vents', 'Air Flow Meter', 'Air Pump', 'Air Ride Compressor', 'Air Shutter', 'Air Tube Resonator', 'Alternator', 'Amplifier or Radio', 'Antenna']

    # This dictionary defines the sections and their respective lines that need to be replaced.
    auto_parts = auto_parts[::-1]

    # Loop through each auto part
for auto_part in auto_parts:
    try:
        modified_lines = []  # Create a separate list for modified lines

        # Replace import statements
        for line in data:
            line = re.sub(
                r"import\s((Map|Table)A)Pillars?\sfrom\s'../../components/layout/((Map|Table)A)Pillars?';",
                lambda match: f"import {auto_part if match.group(2) == 'Map' else 'Table'} from '../../components/layout/{auto_part.replace(' ', '')}';",
                line
            )
            # Debug, Print Out What Was Modified
            print(modified_lines[:10])

        # Replace function section
        for line in modified_lines[:]:
            line = line.replace("APillars", ''.join(word.capitalize() for word in auto_part.split())).replace("a-pillar", auto_part.replace(' ', '-')).replace("loadAPillar", ''.join(word.capitalize() for word in auto_part.split())).replace("a-pillar-count", auto_part.replace(' ', '-'))
            
            # Append the modified line to the new list
            modified_lines.append(line)

            # Debug, Print Out What Was Modified
            print(modified_lines[:50])

        # Replace HTML section
        start_marker = "{/* Start Images */}"
        end_marker = "{/* End Images */}"
        replace_start = False
        
        for line in modified_lines:
            if line.strip() == start_marker:
                replace_start = True
                modified_lines.append(line)
                continue
            elif line.strip() == end_marker:
                replace_start = False
                modified_lines.append(line)
                continue
            if replace_start:
                # Perform specific replacements within the HTML section
                line = re.sub(r"(?i)\bA\s*Pillar\b", ' '.join(word.capitalize() for word in auto_part.split()), line)
                line = re.sub(r"(?i)\bapillar\b", auto_part.lower().replace(' ', '-'), line)
                line = re.sub(r"(?i)\ba\s+pillar\b", auto_part.lower().replace(' ', '-'), line)
                line = re.sub(r"(?i)\bexterior\s+a\s+pillar\s+and\s+interior\s+a\s+pillar\b", auto_parts[(auto_parts.index(auto_part) + 1) % len(auto_parts)].lower().replace(' ', '-'), line)
            modified_lines.append(line)  # Append the modified line to the new list

        # Determine folder name based on auto part name, and convert to lowercase
        folder_name = '-'.join(auto_part.split()).lower()

        # Set absolute path of output folder to root directory
        output_folder_path = "/Users/autopartex/Desktop/AutoPartEx/AutoPartExUtilities/"

        # Check if the output folder exists; if not, create it
        if not os.path.exists(output_folder_path):
            os.mkdir(output_folder_path)

        # Set absolute path of formatted output folder
        formatted_output_folder_path = os.path.join(output_folder_path, folder_name)

        # Check if the formatted output folder exists; if not, create it
        if not os.path.exists(formatted_output_folder_path):
            os.mkdir(formatted_output_folder_path)

        # Set filename of output file
        output_filename = 'index.js'

        # Set output file absolute path within the formatted output folder
        output_path = os.path.join(formatted_output_folder_path, output_filename)

        # Check if the output file exists in the formatted output folder; if not, create it
        if not os.path.exists(output_path):
            with open(output_path, 'w') as f:
                f.writelines(modified_lines)

            # Print the number of lines in the new file
            print(f"{len(modified_lines)} lines written to {os.path.abspath(output_path)}")

        # If the output file exists in the formatted output folder, print a message indicating that it was not created
        else:
            print(f"{output_filename} already exists in the formatted output folder; skipping")
    except Exception as e:
        print(f"An error occurred for auto part: {auto_part}")
        print(e)

        # Continue to the next iteration of the loop
        continue

    # Navigate back to the output_folder_path
    os.chdir(output_folder_path)

# Move the folder to the current working directory
os.rename(
    os.path.join(output_folder_path, formatted_output_folder_path),
    os.path.join(output_folder_path, filename)
)

# Print out the fully modified code
with open('apillarb.js') as f:
    print(f.read()

# This Script Failed 
# It Returns An Empty List
# [], so I You'll Want To Test It Against MKI
