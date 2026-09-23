"""Calculate employee pay from hours worked and an hourly rate."""

try:
    hours = float(input("Enter hours worked: "))
    rate = float(input("Enter hourly rate: "))

    if hours < 0 and rate < 0:
        print("Hours and rate cannot be negative")
    elif hours < 0:
        print("Hours cannot be negative")
    elif rate < 0:
        print("Rate cannot be negative")
    else:
        total_pay = hours * rate

        print("Hours Worked:", hours)
        print("Hourly Rate:", rate)
        print(f"Total Pay: ${total_pay:.2f}")

except ValueError:
    print("Invalid input: enter numeric values")
