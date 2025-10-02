# Split the input string into a list of strings
nums_str = "7 2 1 0 4 2 5".split()
nums_str_2 = "7 2 1 0 4 2".split()

# Convert each string in the list to an integer using list comprehension
numbers = [int(x) for x in nums_str]
numbers_2 = [int(x) for x in nums_str_2]

# Print the full lists to verify the conversion
print(numbers)     # Output: [7, 2, 1, 0, 4, 2, 5]
print(numbers_2)   # Output: [7, 2, 1, 0, 4, 2]

# Print the second half of each list
# [3::] means slicing the list starting from index 3 to the end
print(numbers[3::])     # Output: [0, 4, 2, 5]
print(numbers_2[3::])   # Output: [0, 4, 2]

# Optional: print second half without brackets using unpacking
print(*numbers[3::])    # Output: 0 4 2 5
print(*numbers_2[3::])  # Output: 0 4 2



