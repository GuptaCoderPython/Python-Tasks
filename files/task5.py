file_name = "neeraj_example.txt"

with open(file_name, 'r') as file:
    file.seek(10)
    content = file.read()
    print(content)