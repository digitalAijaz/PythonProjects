print("Welcome to the Tip Calculator!")

# Get the bill amount from the user
bill = float(input("What is the total bill amount in $: "))

# Get the number of people to split the bill
num_of_people = int(input("How many people to split the bill: "))

# Get the tip percentage from the user
tip_percentage = float(input("What percentage tip would you like to give? "))

# Calculate the total bill amount including tip
total_bill = bill * (1 + tip_percentage / 100)

# Calculate the individual contribution
individual_contribution = round(total_bill / num_of_people, 2)

# Display the individual contribution with 2 decimal places
print(f"Each person should pay ${individual_contribution:.2f}")