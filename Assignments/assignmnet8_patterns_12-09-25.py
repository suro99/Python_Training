# Assignment 1: List All .txt Files and Check for a Word using glob + re.search
# Write a script to:
# - Find all .txt files in a folder.
# - Check if any file contains the word "Python".
# - Print the file name if the word is found
 
 
# Assignment 2: 
# Match File Names Using re.match
# List all files in a folder using glob, and print only the ones that start with "data_" and end with ".csv".
 
 
# Assignment 3: 
# Validate Phone Numbers with re.match
# Given a list of phone numbers, print only the ones that match this format:
# (123) 456-7890

import glob
import re

# Assignment 1:
def find_txt_files_with_word(folder_path, word):
    txt_files = glob.glob(f"{folder_path}/*.txt")
    for file in txt_files:
        with open(file, 'r') as f:
            content = f.read()
            if re.search(rf'\b{word}\b', content):
                print(f"'{word}' found in: {file}")

find_txt_files_with_word('/home/kolkata/Python', 'firstsecondThird')

# Assignment 2:
def list_data_csv_files(folder_path):
    all_files = glob.glob(f"{folder_path}/*")
    pattern = r'^data_.*\.csv$'
    for file in all_files:
        if re.match(pattern, file):
            print(f"Matched file: {file}")

list_data_csv_files('/home/kolkata/Python/')

# Assignment 3:
def validate_phone_numbers(phone_numbers):
    for number in phone_numbers:
        if re.match(r'^\(\d{3}\) \d{3}-\d{4}$', number):
            print(f"Valid phone number: {number}")
        else:
            print(f"Invalid phone number: {number}")


phone_numbers = ["(123) 456-7890", "(987) 654-3210", "123-456-7890"]
validate_phone_numbers(phone_numbers)