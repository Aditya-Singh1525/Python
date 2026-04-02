def get_positive_float(prompt):
    while True:
        val = input(prompt)
        try:
            val = float(val)
            if val > 0:
                return val
            else:
                print("Please enter a value greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a number.")


principle = get_positive_float("Enter the principle:")
rate = get_positive_float("Enter the rate of interest:")
time = get_positive_float("Enter the time of interest in years:")


result = principle * (1 + rate / 100) ** time

print(f"\nBalance after {time} year/s:${result:.2f}")
