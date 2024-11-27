import re

# 1. Different Ways of Creating a String
string1 = 'Hello World'
string2 = "Hello World"
string3 = '''Hello
World'''

# 2. Concatenating Two Strings Using + Operator
str1 = "Hello"
str2 = "World"
concatenated = str1 + " " + str2

# 3. Finding the Length of the String
length = len(concatenated)

# 4. Extract a String Using Substring
substring = concatenated[0:5]

# 5. Searching in Strings Using index()
position = concatenated.index("World")

# 6. Matching a String Against a Regular Expression
pattern = re.compile(r'\d+')
match = pattern.match("123abc")

# 7. Comparing Strings
str3 = "apple"
str4 = "banana"

# 8. Trimming Strings with strip()
trimmed = "  Hello World  ".strip()

# 9. Replacing Characters in Strings with replace()
replaced_text = concatenated.replace("World", "Python")

# 10. Splitting Strings with split()
words = concatenated.split(" ")

# 11. Converting Integer Objects to Strings
num = 123
str_num = str(num)

# 12. Converting to Uppercase and Lowercase
upper_case = concatenated.upper()
lower_case = concatenated.lower()

print("1. Concatenated String:", concatenated)
print("2. Length of the String:", length)
print("3. Substring (0 to 5):", substring)
print("4. Position of 'World':", position)
if match:
    print("5. Regex Match Found:", match.group())
print("6. Comparing 'apple' and 'banana':", str3 == str4)
print("7. Does it start with 'Hello'? :", concatenated.startswith('Hello'))
print("8. Does it end with 'World'? :", concatenated.endswith('World'))
print("9. Trimmed String:", trimmed)
print("10. Replaced String:", replaced_text)
print("11. Splitted Words:", words)
print("12. Integer to String:", str_num)
print("13. Uppercase:", upper_case)
print("14. Lowercase:", lower_case)
