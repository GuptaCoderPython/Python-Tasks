file_name = "python_tasks.txt"

with open(file_name, 'w') as file:
    text = input("Enter the text to write to the file: ")
    file.write(text)
    print(f"Text written to {file_name}")