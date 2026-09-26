"""Provide an interactive toolkit for common engineering unit conversions."""


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def kilometres_to_miles(kilometres):
    miles = kilometres * 0.621371
    return miles


def miles_to_kilometres(miles):
    kilometres = miles * 1.60934
    return kilometres


def display_menu():
    print("\nEngineering Conversion Toolkit")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Kilometres to miles")
    print("4. Miles to kilometres")
    print("5. Exit")


def main():
    while True:
        display_menu()

        try:
            choice = int(input("\nSelect an option: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

        if choice == 5:
            print("Goodbye!")
            break

        elif choice == 1:
            try:
                celsius = float(input("Enter temperature in Celsius: "))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"{celsius:.2f} C = {fahrenheit:.2f} F")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif choice == 2:
            try:
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                celsius = fahrenheit_to_celsius(fahrenheit)
                print(f"{fahrenheit:.2f} F = {celsius:.2f} C")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif choice == 3:
            try:
                kilometres = float(input("Enter distance in kilometres: "))
                miles = kilometres_to_miles(kilometres)
                print(f"{kilometres:.2f} km = {miles:.2f} mi")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif choice == 4:
            try:
                miles = float(input("Enter distance in miles: "))
                kilometres = miles_to_kilometres(miles)
                print(f"{miles:.2f} mi = {kilometres:.2f} km")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        else:
            print("Invalid option. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()
