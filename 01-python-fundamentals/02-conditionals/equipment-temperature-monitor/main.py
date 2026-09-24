"""Classify equipment temperature and display its operating status."""

try:
    temperature = float(input("Enter equipment temperature (C): "))

    if temperature < 20:
        print("WARNING: Temperature too low")
    elif temperature <= 70:
        print("Equipment temperature normal")
    elif temperature <= 80:
        print("WARNING: Equipment temperature high")
    else:
        print("CRITICAL: Equipment overheating")

except ValueError:
    print("Invalid input: enter a numeric temperature")
