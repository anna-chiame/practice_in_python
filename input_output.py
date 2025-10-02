# Print the menu of colors for the user to choose
print("Choose your favourite color:\n"
      "1. Red\n"
      "2. Blue\n"
      "3. White\n"
      "4. Black\n")

# Function to determine the favourite color based on user input
def fav_color(number):
    # Check if the input consists only of digits
    if number.isdigit():
        # Convert input from string to integer
        number = int(number)
        # Check each option and print the corresponding color
        if number == 1:
            print("Your favourite color is Red")
        elif number == 2:
            print("Your favourite color is Blue")
        elif number == 3:
            print("Your favourite color is White")
        elif number == 4:
            print("Your favourite color is Black")
        else:
            # If the number is not in the range 1–4
            print("Please choose a number from 1 to 4")
    else:
        # If input contains non-digit characters
        print("Please choose only number from list")

# Ask the user to choose a color
number = input("Choose your favourite color\n")
# Call the function to check and print the favourite color
fav_color(number)





