file_name = "neeraj_example.txt"

with open(file_name, 'rb') as file:
    file.seek(5)
    content = file.read(10)
    print(content)