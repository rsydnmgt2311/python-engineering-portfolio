# Engineering Conversion Toolkit

A command-line Python application that performs common temperature and distance conversions through a reusable, function-based design.

## Features

- Converts Celsius to Fahrenheit.
- Converts Fahrenheit to Celsius.
- Converts kilometres to miles.
- Converts miles to kilometres.
- Continues running until the user chooses to exit.
- Rejects unsupported menu selections.
- Handles non-numeric input without terminating unexpectedly.
- Formats conversion results to two decimal places.

## Skills demonstrated

- Function definition and invocation
- Parameters and return values
- Menu-driven program flow
- `while` loops
- Conditional statements
- Exception handling with `try` and `except`
- Numeric calculations and formatted output
- Python's `__name__ == "__main__"` entry-point pattern

## Conversion formulas

```text
Fahrenheit = (Celsius × 9 / 5) + 32
Celsius = (Fahrenheit - 32) × 5 / 9
Miles = Kilometres × 0.621371
Kilometres = Miles × 1.60934
```

## Run the program

From this directory, run:

```text
python main.py
```

## Example

```text
Engineering Conversion Toolkit
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Kilometres to miles
4. Miles to kilometres
5. Exit

Select an option: 4
Enter distance in miles: 10
10.00 mi = 16.09 km
```

The menu appears again after each completed conversion. Selecting option `5` ends the program.

## Validation

The completed program was checked with:

- standard temperature and distance values;
- freezing and boiling temperature reference points;
- negative temperatures;
- unsupported menu selections;
- decimal and text menu entries;
- non-numeric conversion values;
- immediate and normal exit behavior.

## Project files

```text
engineering-conversion-toolkit/
├── main.py
└── README.md
```
