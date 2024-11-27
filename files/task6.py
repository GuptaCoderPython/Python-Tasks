import os

file_name = "neeraj_example.txt"

if os.access(file_name, os.R_OK):
    print(f"{file_name} is readable.")
else:
    print(f"{file_name} is not readable.")

if os.access(file_name, os.W_OK):
    print(f"{file_name} is writable.")
else:
    print(f"{file_name} is not writable.")