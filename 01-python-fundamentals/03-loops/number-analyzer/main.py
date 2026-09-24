"""Analyze a sequence of numbers entered by the user."""

count = 0
total = 0.0
largest = None
smallest = None

while True:
    user_input = input("Enter a number or 'done': ").strip()

    if user_input.lower() == "done":
        break

    try:
        number = float(user_input)
    except ValueError:
        print("Invalid input: enter a number or 'done'")
        continue

    count = count + 1
    total += number

    if largest is None or number > largest:
        largest = number

    if smallest is None or number < smallest:
        smallest = number

if count == 0:
    print("No valid numbers were entered")
else:
    average = total / count
    print("\nNumber Summary")
    print(f"Count: {count}")
    print(f"Total: {total:.2f}")
    print(f"Average: {average:.2f}")
    print(f"Largest: {largest:.2f}")
    print(f"Smallest: {smallest:.2f}")
