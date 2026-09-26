"""Classify sensor temperatures and summarize valid readings."""

reading_count = 0
low_count = 0
normal_count = 0
high_count = 0
temperature_total = 0.0
minimum_temperature = None
maximum_temperature = None

while True:
    user_input = input("Enter sensor temperature or 'done': ").strip()

    if user_input.lower() == "done":
        break

    try:
        temperature = float(user_input)
    except ValueError:
        print("Invalid input: enter a temperature or 'done'")
        continue

    if temperature < 20:
        low_count += 1
    elif temperature <= 70:
        normal_count += 1
    else:
        high_count += 1

    reading_count += 1
    temperature_total += temperature

    if minimum_temperature is None or temperature < minimum_temperature:
        minimum_temperature = temperature

    if maximum_temperature is None or temperature > maximum_temperature:
        maximum_temperature = temperature

if reading_count == 0:
    print("No valid sensor readings were entered")
else:
    average_temperature = temperature_total / reading_count
    print("\nSensor Reading Summary")
    print(f"Total readings: {reading_count}")
    print(f"Low readings: {low_count}")
    print(f"Normal readings: {normal_count}")
    print(f"High readings: {high_count}")
    print(f"Average temperature: {average_temperature:.2f} C")
    print(f"Minimum temperature: {minimum_temperature:.2f} C")
    print(f"Maximum temperature: {maximum_temperature:.2f} C")
