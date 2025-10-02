import sys
import os

# Get the absolute path of the current directory
project_root = os.path.abspath(os.getcwd())

# Read all input from stdin
input_text = sys.stdin.read()

# Replace the placeholder with the project root path
output_text = input_text.replace("${PROJECT_ROOT}", project_root)

# Output to stdout
print(output_text, end='')
