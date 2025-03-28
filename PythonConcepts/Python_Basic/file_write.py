"""
This is a file that writes to a file.
"""

import os

print(os.getcwd())
file_path = os.path.join(
    os.path.dirname(__file__), "Data.csv"
)  # This is the path to the file

with open(file_path, "r") as file_data:
    """
    This is a context manager that opens a file and reads it.
    """
    all_data = file_data.read()

all_data = [content + ",\n" for content in all_data.split("\n")]
print(all_data)

with open(file_path, "w") as file_data:
    """
    This is a context manager that opens a file and writes to it.
    """
    file_data.writelines(all_data)

with open(file_path, "a") as file_data:
    """
    This is a context manager that opens a file and appends to it.
    """
    file_data.write("]")
