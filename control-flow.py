# Problem 0: Example
#
# This is a practice problem to help you understand how to write code in a 
# provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting
# message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
  # Declare a variable python_is_fun and set it to True
  python_is_fun = True

  # Use a conditional statement to check if python_is_fun is True
  if python_is_fun:
    # If True, print the message
    print("Python is fun!")

# Call the function
print_greeting()


# Problem 1: Vowel or consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and 
#   determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user in the above
#   messages.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels. You may need to look up
#   how to use this online.
# - Ensure your code provides feedback for non-alphabetical or invalid entries.

def check_letter():
    """
    Determines if a user-provided letter is a vowel or a consonant.

    Handles both uppercase and lowercase letters and provides feedback
    for non-alphabetical entries.
    """
    user_input = input("Enter a single letter (a-z or A-Z): ").lower()

    if len(user_input) != 1 or not user_input.isalpha():
        print("Invalid entry. Please enter a single alphabetical character.")
    elif user_input in ('a', 'e', 'i', 'o', 'u'):
        print(f"The letter {user_input} is a vowel.")
    else:
        print(f"The letter {user_input} is a consonant.")

# Call the function
check_letter()



# Problem 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a
# user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative 
#   numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting
#   age.
# - Print a message indicating whether the user is eligible to vote based on the
#   entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure that you handle any 
#   conversion errors gracefully. You may need to look up how to do this online.
# - Use a conditional statement to check if the age meets the minimum voting age
#   requirement.

def check_voting_eligibility():
    """
    Determines if a user is old enough to vote based on their input age.
    """
    VOTING_AGE = 18  # Set the minimum voting age

    while True:  # Loop until a valid input is received
        age_input = input("Please enter your age: ")

        try:
            age = int(age_input)  # Convert input to an integer

            if age < 0:
                # Handle negative numbers
                print("Error: Age cannot be a negative number. Please enter a valid, positive age.")
                continue  # Restart the loop to ask for input again
            elif age < VOTING_AGE:
                # User is not eligible
                print(f"You are {age} years old. You are not eligible to vote yet.")
            else:
                # User is eligible
                print(f"You are {age} years old. You are eligible to vote!")
            break  # Exit the loop if a valid age (positive integer) was processed

        except ValueError:
            # Handle non-integer input (e.g., text, decimals)
            print("Error: Invalid input. Please enter a whole number for your age.")

# Call the function
check_voting_eligibility()



# Problem 3: Calculate dog years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's
# age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the
#   dog's age.

def calculate_dog_years():
    """
    Calculates a dog's age in dog years based on user input.

    The first two years of the dog's life count as 10 dog years each.
    Each subsequent year counts as 7 dog years.
    """
    try:
        # Prompt the user for input and convert it to an integer
        human_age = int(input("Input a dog's age: "))
        dog_years = 0

        if human_age <= 0:
            print("Please enter a valid age greater than zero.")
            return

        # Calculate dog years based on the specified rules
        if human_age <= 2:
            dog_years = human_age * 10
        else:
            # First two years account for 20 dog years
            dog_years = 20
            # Each subsequent year adds 7 dog years
            dog_years += (human_age - 2) * 7

        # Print the final result
        print(f"The dog's age in dog years is {dog_years}.")

    except ValueError:
        # Handle cases where the input is not a valid integer
        print("Invalid input. Please enter a numerical value for the age.")

# Call the function to run the program
calculate_dog_years()



# Problem 4: Weather advice
#
# Write a Python script named `weather_advice` that provides clothing advice
# based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle
#   multiple conditions.

def weather_advice():
    # Prompt user for input on weather conditions, converting to lowercase for consistent comparison
    is_cold_input = input("Is it cold? (yes/no): ").lower()
    is_raining_input = input("Is it raining? (yes/no): ").lower()

    # Determine boolean values from user input
    is_cold = (is_cold_input == "yes")
    is_raining = (is_raining_input == "yes")

    # Use logical operators in if/elif/else statements to provide advice
    if is_cold and is_raining:
        print("Wear a waterproof coat.")
    elif is_cold and not is_raining:
        print("Wear a warm coat.")
    elif not is_cold and is_raining:
        print("Carry an umbrella.")
    else:
        # This condition covers the case where it is NOT cold AND NOT raining
        print("Wear light clothing.")

# Call the function to run the script
weather_advice()



# Problem 5: What's the season?
#
# Write a Python function named `determine_season` that figures out the season
# based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three
#   characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month:
#   "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in
#   <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure you validate the user's input and handle unexpected inputs
#   gracefully.

def determine_season():
    """
    Prompts the user for a month and day, then determines and prints the corresponding season.
    """
    # Define valid months as a tuple for easy 'in' checking and order
    valid_months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

    # --- Input and Validation for Month ---
    while True:
        month_input = input("Enter the month of the year (Jan - Dec):").strip().capitalize()
        if month_input in valid_months:
            break
        else:
            print(f"'{month_input}' is not a valid month abbreviation. Please use Jan, Feb, etc.")

    # --- Input and Validation for Day ---
    while True:
        day_input = input("Enter the day of the month:").strip()
        try:
            day = int(day_input)
            if 1 <= day <= 31: # Basic day range validation
                break
            else:
                print(f"'{day_input}' is not a valid day. Please enter a number between 1 and 31.")
        except ValueError:
            print(f"'{day_input}' is not a valid number. Please enter an integer for the day.")

    # --- Season Determination Logic ---
    month = month_input
    season = ""

    if month in ("Jan", "Feb"):
        season = "Winter"
    elif month == "Mar":
        # Winter until March 19th
        season = "Spring" if day >= 20 else "Winter"
    elif month in ("Apr", "May"):
        season = "Spring"
    elif month == "Jun":
        # Spring until June 20th
        season = "Summer" if day >= 21 else "Spring"
    elif month in ("Jul", "Aug"):
        season = "Summer"
    elif month == "Sep":
        # Summer until September 21st
        season = "Fall" if day >= 22 else "Summer"
    elif month in ("Oct", "Nov"):
        season = "Fall"
    elif month == "Dec":
        # Fall until December 20th
        season = "Winter" if day >= 21 else "Fall"

    # --- Print the Result ---
    print(f"{month} {day} is in {season}.")

# Call the function as required by the problem prompt
determine_season()
