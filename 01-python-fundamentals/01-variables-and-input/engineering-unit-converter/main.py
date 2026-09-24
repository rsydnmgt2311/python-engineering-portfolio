"""Convert common engineering measurements between metric and imperial units."""

try:
    celsius = float(input("Enter temperature in Celsius: "))
    millimetres = float(input("Enter length in millimetres: "))
    kilograms = float(input("Enter mass in kilograms: "))

    fahrenheit = celsius * 9 / 5 + 32
    inches = millimetres / 25.4
    pounds = kilograms * 2.20462

    print("\nConversion Results")
    print(f"Temperature: {celsius:.2f} C = {fahrenheit:.2f} F")
    print(f"Length: {millimetres:.2f} mm = {inches:.3f} in")
    print(f"Mass: {kilograms:.2f} kg = {pounds:.2f} lb")

except ValueError:
    print("Invalid input: enter numeric values")
