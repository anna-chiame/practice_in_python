# Read input from the user
num = input("Input number: ")

# Validate that input is an integer (allow negative sign)
if num.lstrip('-').isdigit():
    # Convert string to integer
    num = int(num)

    # Print the results using formatted strings
    print(f"Input number is {num}\n"
          f"Number before is {num - 1}\n"
          f"Number next is {num + 1}\n")
else:
    # If the input is invalid, show an error message
    print("Input only integers")

