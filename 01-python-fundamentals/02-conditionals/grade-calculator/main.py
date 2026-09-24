"""Convert a numeric score from 0.0 to 1.0 into a letter grade."""

try:
    score = float(input("Enter score (0.0-1.0): "))

    if score < 0.0 or score > 1.0:
        print("Invalid score: enter a value from 0.0 to 1.0")
    elif score >= 0.9:
        print("Grade: A")
    elif score >= 0.8:
        print("Grade: B")
    elif score >= 0.7:
        print("Grade: C")
    elif score >= 0.6:
        print("Grade: D")
    else:
        print("Grade: F")

except ValueError:
    print("Invalid input: enter a numeric score")
