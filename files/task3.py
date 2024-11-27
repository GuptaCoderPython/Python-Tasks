file_name = "neeraj_example.txt"

with open(file_name, 'rb') as file:
    file_content = file.read()
    print(file_content)