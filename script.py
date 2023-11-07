import sys

label = sys.argv[1]

# Read the RST file
with open('path/to/your/file.rst', 'r') as file:
    rst_content = file.read()

# Update a specific placeholder with the label value
placeholder = "Label Placeholder: "
new_rst_content = rst_content.replace(placeholder, f"{placeholder}{label}")

# Write the updated content back to the RST file
with open('path/to/your/file.rst', 'w') as file:
    file.write(new_rst_content)
