"""

The "split" method is exclusive to string objects. When applied to a string, it utilizes a pointer mechanism. 
It starts at the 0th index and captures the data between the beginning of the string and the first occurrence 
of the delimiter, placing it in the list. 
The pointer then advances to the position after the first occurrence.

Subsequently, it includes the data between the pointer's current position (after the first occurrence) 
and the second occurrence of the delimiter in the list. The pointer advances again, repeating this process 
until the last occurrence of the delimiter.

Finally, the data between the pointer's last position (after the last occurrence) and the end of the string 
is added to the list. This results in a list of substrings generated from the original string based on the 
occurrences of the specified delimiter and the pointer's movements.
"""

# ---The syntax for the "split" method is as follows:
# ->>>string.split(separator, maxsplit)
data = "Hello"
print(data.split("l"))
["He", "", "o"]

"""
"separator" : This is the delimiter on which the string will be split. If the separator is not specified, 
the string is split at whitespace characters (spaces, tabs, and newlines by default).

"maxsplit" (optional): This parameter specifies the maximum number of splits to be done.
If not provided, there is no limit to the number of splits.

The `split` method is specifically designed for string objects in Python. If you attempt to use it on an object
of a different type, you will likely encounter an AttributeError.

"""


a = "Helsdsloslsd"
print(a.split("l", 1))
["He", "sdsloslsd"]


print(a.split("l", 2))
["He", "sds", "oslsd"]

print(a.split("l", 3))
["He", "sds", "os", "sd"]

print(a.split("l"))
["He", "sds", "os", "sd"]
