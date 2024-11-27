def even_odd(num):
    switch = {
        0: "Even",
        1: "Odd"
    }
    return switch[num % 2]

num = int(input("Enter a number: "))
print(f"The number is {even_odd(num)}")
