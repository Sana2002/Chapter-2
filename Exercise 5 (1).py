price_per_usb_stick = 6  # price of each USB stick in pounds
budget = 50  # amount of money the girl has in pounds

# Calculate how many USB sticks the girl can buy
num_usb_sticks = budget // price_per_usb_stick

# Calculate how much money the girl has left
remaining_budget = budget % price_per_usb_stick

# Print the results
print(f"The girl can buy {num_usb_sticks} USB sticks.")
print(f"She will have {remaining_budget} pounds left.")