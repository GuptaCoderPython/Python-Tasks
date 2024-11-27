# Array Operations

# 1. Function to add integer values of an array
def sum_array(arr):
    return sum(arr)

# 2. Function to calculate the average value of an array of integers
def average_array(arr):
    return sum(arr) / len(arr) if len(arr) > 0 else 0

# 3. Program to find the index of an array element
def find_index(arr, value):
    try:
        return arr.index(value)
    except ValueError:
        return -1  # Element not found

# 4. Function to test if the array contains a specific value
def contains_value(arr, value):
    return value in arr

# 5. Function to remove a specific element from an array
def remove_element(arr, value):
    if value in arr:
        arr.remove(value)
    return arr

# 6. Function to copy an array to another array
def copy_array(arr):
    return arr.copy()

# 7. Function to insert an element at a specific position in the array
def insert_element(arr, index, value):
    arr.insert(index, value)
    return arr

# 8. Function to find the minimum and maximum value of an array
def min_max_array(arr):
    return min(arr), max(arr)

# 9. Function to reverse an array of integer values
def reverse_array(arr):
    return arr[::-1]

# 10. Function to find the duplicate values of an array
def find_duplicates(arr):
    seen = set()
    duplicates = set()
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

# 11. Program to find the common values between two arrays
def common_values(arr1, arr2):
    return list(set(arr1) & set(arr2))

# 12. Method to remove duplicate elements from an array
def remove_duplicates(arr):
    return list(set(arr))

# 13. Method to find the second largest number in an array
def second_largest(arr):
    unique_arr = list(set(arr))
    unique_arr.sort()
    return unique_arr[-2] if len(unique_arr) > 1 else None

# 14. Same method to find the second largest number in an array
def second_largest_v2(arr):
    return second_largest(arr)

# 15. Method to find the number of even and odd numbers in an array
def count_even_odd(arr):
    even = sum(1 for num in arr if num % 2 == 0)
    odd = len(arr) - even
    return even, odd

# 16. Function to get the difference of the largest and smallest value
def diff_largest_smallest(arr):
    return max(arr) - min(arr) if arr else 0

# 17. Method to verify if the array contains two specified elements (12, 23)
def contains_two_elements(arr, elem1, elem2):
    return elem1 in arr and elem2 in arr

# 18. Program to remove the duplicate elements and return the new array
def remove_duplicates_return_new(arr):
    return list(set(arr))

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 5, 6, 7, 8]
    arr2 = [3, 4, 5, 9, 10]

    print("1. Sum of array:", sum_array(arr))
    print("2. Average of array:", average_array(arr))
    print("3. Index of 4:", find_index(arr, 4))
    print("4. Contains 5:", contains_value(arr, 5))
    print("5. Array after removing 5:", remove_element(arr.copy(), 5))
    print("6. Copy of array:", copy_array(arr))
    print("7. Insert 99 at position 2:", insert_element(arr.copy(), 2, 99))
    print("8. Min and Max:", min_max_array(arr))
    print("9. Reversed array:", reverse_array(arr))
    print("10. Duplicates in array:", find_duplicates(arr))
    print("11. Common values between arrays:", common_values(arr, arr2))
    print("12. Array after removing duplicates:", remove_duplicates(arr))
    print("13. Second largest number:", second_largest(arr))
    print("14. Second largest number (v2):", second_largest_v2(arr))
    print("15. Count of even and odd numbers:", count_even_odd(arr))
    print("16. Difference between largest and smallest:", diff_largest_smallest(arr))
    print("17. Contains 12 and 23:", contains_two_elements(arr, 12, 23))
    print("18. Array after removing duplicates (new array):", remove_duplicates_return_new(arr))