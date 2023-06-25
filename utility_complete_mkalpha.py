import os
import re

# define the name of the file and folder to be used
filename = 'apillarb.js'

# open and read the content of apillarb.js
with open(filename, 'r') as f:
    data = f.readlines()

# debug
# lets see if this actually opened the correct file
print(data[:10])

# declare empty list to store auto part names
auto_parts = []

# read auto part names from part-names.js file
with open('part-names.js') as f:
    auto_part_data = f.read()

    # find all auto part names using regular expression
    # auto_part_matches = re.findall(r"partname: '(.+?)'", auto_part_data)

    # find all auto part names using regular expression
    auto_part_matches = re.findall(r"partname:(?:\s*)'(.+?)'", auto_part_data)

    # debug feature
    print(auto_part_matches)

    # re.findall() to obtain all matches and then filtered out any empty matches using a list comprehension. 
    # This ensures that the auto part names are preserved in the order they appear in the part-names.js file.
    auto_parts = [match for match in auto_part_matches if match]

    print(auto_parts[:10])

    # reformat auto part names for proper capitalization and list items with hyphens
    auto_parts = []
    
    for part in auto_part_matches:
        if '-' in part:
            # format list item with hypens
            new_part = '-'.join([word.capitalize() for word in part.split('-')])
        else:
            # apply proper capitalization for auto part (capitalization preserved for all occurrences of auto part name)
            new_part = re.sub(r"(?i)\b(A Pillars?|APillars?|A Pillar|APillar)\b", 
                      lambda match: match.group(0).upper() if match.group(0).isupper() else match.group(0).replace(match.group(0), match.group(0).capitalize()), 
                      part)
        auto_parts.append(new_part)

# add custom auto part names to auto_parts list
# commenting out for now, initially I was going to add them manually
# the above function opens up the part-names js file to grap the string by regex pattern

# auto_parts.extend(['apillar', 'engine', 'transmission', 'transfer case', 'alternator', 'ac compressor', 'radiator'])

# reverse the order of the auto parts list
# auto_parts = list(reversed(auto_parts))
auto_parts = auto_parts[::-1]

# loop through each auto part
for auto_part in auto_parts:
    try:
        output_lines = []

        # replace parts of apillarb.js with the auto part name
        for line in data:
            # Replace auto part name in image file paths
            # line = re.sub(r"\bA[ -]?Pillars?\b|\ba-pillars?\b|\ba[- ]?pillar(?:s)?\b|\bapillars?\b", 
            #               f"{auto_part if 'apillar' not in line.lower() else '-'.join(auto_part.split())}", 
            #               line, flags=re.IGNORECASE)
            # output_lines.append(line)
            
            line = re.sub(r"\bA[ -]?Pillars?\b|\ba[- ]?pillar(?:s)?\b|\bapillar\b(?=\})|\bMapAPillar\b|\bTableAPillars\b|\blistAPillar\b|\bloadAPillar\b", 
              lambda match: f"{auto_part.title().replace(' ', '')}" if match.group(0).isupper() else f"{auto_part.lower().replace(' ', '')}", 
              line, flags=re.IGNORECASE)
            output_lines.append(line)


        # determine folder name based on auto part name, and convert to lowercase
        folder_name = '-'.join(auto_part.split()).lower()

        # set absolute path of output folder to root directory
        output_folder_path = "/Users/autopartex/Desktop/AutoPartEx/AutoPartExUtilities/"

        # check if the output folder exists; if not, create it
        if not os.path.exists(output_folder_path):
            os.mkdir(output_folder_path)

        # set absolute path of formatted output folder
        formatted_output_folder_path = os.path.join(output_folder_path, folder_name)

        # check if the formatted output folder exists; if not, create it
        if not os.path.exists(formatted_output_folder_path):
            os.mkdir(formatted_output_folder_path)

        # set filename of output file
        output_filename = 'index.js'

        # set output file absolute path within the formatted output folder
        output_path = os.path.join(formatted_output_folder_path, output_filename)

        # check if the output file exists in the formatted output folder; if not, create it
        if not os.path.exists(output_path):
            with open(output_path, 'w') as f:
                f.writelines(output_lines)

            # print the number of lines in the new file
            print(f"{len(output_lines)} lines written to {os.path.abspath(output_path)}")

        # if the output file exists in the formatted output folder, print a message indicating that it was not created
        else:
            print(f"{output_filename} already exists in the formatted output folder; skipping")
    except Exception as e:
        print(f"An error occurred for auto part: {auto_part}")
        print(e)

        # continue to the next iteration of the loop
        continue
        
    # navigate back to the output_folder_path
    os.chdir(output_folder_path)
    

# move the folder to the current working directory
os.rename(
    os.path.join(output_folder_path, formatted_output_folder_path),
    os.path.join(output_folder_path, filename)
)

# print out the fully modified code
# with open('apillarb.js') as f:
# print(f.read())