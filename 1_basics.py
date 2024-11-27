#Printing my first-second name:
print("Neeraj,\nGupta")
#comments:
# This is a single-line comment

"""
This is a multi-line comment.
We can use triple quotes to create comments
that span multiple lines.
"""
print("Comments demonstrated")

#Variables:
# Defining variables of different data types
int_var = 10  # Integer
bool_var = True  # Boolean
char_var = 'A'  # Character
float_var = 3.14  # Float
double_var = 1.23456789  # Double (Python treats all floats as double-precision)

my_string="String" #String;
# Printing the variables
print("Integer:", int_var)
print("Boolean:", bool_var)
print("Character:", char_var)
print("Float:", float_var)
print("Double:", double_var)
print("string",my_string")

# Global variable
var = "Global Variable"

def my_function():
    # Local variable
    var = "Local Variable"
    print("Inside the function:", var)

my_function()
print("Outside the function:", var)
#global  variables are which define out of the function: and local variables are which define in function.