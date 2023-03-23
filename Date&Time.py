import datetime

# Define the number of days to add
num_days = 10

# Get the current date
current_date = datetime.date.today()

# Add the specified number of days to the current date
new_date = current_date + datetime.timedelta(days=num_days)

# Print the resulting day of the week
print("The resulting date is:", new_date.strftime("%A"))
