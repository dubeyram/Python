"""
This is a file that contains the code for the regex concepts.
"""

import re

# Basic Regex Examples

# 1. Matching a simple string
pattern = r"hello"
text = "hello world"
match = re.search(pattern, text)
if match:
    print("Basic Match:", match.group())

# 2. Matching a digit
pattern = r"\d"
text = "There are 2 apples"
match = re.search(pattern, text)
if match:
    print("Digit Match:", match.group())

# 3. Matching a word
pattern = r"\bworld\b"
text = "hello world"
match = re.search(pattern, text)
if match:
    print("Word Match:", match.group())

# Intermediate Regex Examples

# 4. Matching an email address
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
text = "Please contact us at support@example.com"
match = re.search(pattern, text)
if match:
    print("Email Match:", match.group())

# 5. Matching a phone number (US format)
pattern = r"\(\d{3}\) \d{3}-\d{4}"
text = "Call me at (123) 456-7890"
match = re.search(pattern, text)
if match:
    print("Phone Number Match:", match.group())

# 6. Matching a URL
pattern = r"https?://(?:www\.)?\w+\.\w+"
text = "Visit our website at https://www.example.com"
match = re.search(pattern, text)
if match:
    print("URL Match:", match.group())

# Advanced Regex Examples

# 7. Matching a date (MM/DD/YYYY)
pattern = r"\b(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}\b"
text = "Today's date is 02/28/2025"
match = re.search(pattern, text)
if match:
    print("Date Match:", match.group())

# 8. Matching a time (HH:MM AM/PM)
pattern = r"\b(0[1-9]|1[0-2]):[0-5][0-9] (AM|PM)\b"
text = "The meeting is scheduled at 09:30 AM"
match = re.search(pattern, text)
if match:
    print("Time Match:", match.group())

# 9. Matching an IP address
pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
text = "The server IP is 192.168.1.1"
match = re.search(pattern, text)
if match:
    print("IP Address Match:", match.group())

# 10. Matching a hexadecimal color code
pattern = r"#[0-9a-fA-F]{6}\b"
text = "The color code is #AABBCC"
match = re.search(pattern, text)
if match:
    print("Hex Color Match:", match.group())
