# ABC.py — Simple CLI number operator script

Description
-----------
`ABC.py` is a small command-line Python script intended to apply an arithmetic operator to a sequence of numbers entered by the user. The script prompts the user for a list of numbers and an operator, then computes and prints the result.

Requirements
------------
- Python 3.x

How it should work (intended behavior)
-------------------------------------
1. Prompt the user to enter numbers as space-separated values, e.g.:
   - Input prompt: `number input karo:`
   - Example: `1 2 3 4`
2. Prompt the user to enter an operator from the set:
   - `+`, `-`, `*`, `/`, `//`, `%`, `**`
3. Apply the operator to the list of numbers (left-to-right for non-commutative operators) and print the result.

Usage example (intended)
------------------------
Run the script:
```bash
python ABC.py
```

Interactive session (example):
```
number input karo: 2 3 4
Operator (+ - * / // % **): *
Result: 24.0
```

Known issues in the repository version
-------------------------------------
The current `ABC.py` in the repository contains several bugs and usability issues:
- The `operator` variable is set to the literal string `"Operator(+ - * / // % **):"` instead of reading input from the user. That means the script never actually receives the operator choice.
- The loop `for n in number[:1]:` only iterates over the first number and therefore will not apply the operation across the full list.
- `result` is initialized to `number[0]` and then the code tries to operate using the first number again, producing incorrect results for many operations.
- No validation for empty input or invalid numbers.
- No handling of division by zero.
- Uses `int` mapping — this means fractional inputs are rejected. In many use-cases using `float` is preferable.

Suggested fixes
---------------
Below is a corrected and more robust version of the script. It:
- Reads operator input correctly
- Validates input
- Uses `float` for numeric inputs (change to `int` if integers are required)
- Applies operations left-to-right for non-commutative operators
- Handles division by zero

```python
#!/usr/bin/env python3
def main():
    s = input("Enter numbers (space-separated): ").strip()
    if not s:
        print("No numbers provided.")
        return
    try:
        numbers = list(map(float, s.split()))
    except ValueError:
        print("Invalid numbers. Please enter space-separated numeric values.")
        return

    op = input("Operator (+ - * / // % **): ").strip()
    if op not in {"+", "-", "*", "/", "//", "%", "**"}:
        print("Unsupported operator.")
        return

    # Handle operators
    if op == "+":
        result = sum(numbers)
    elif op == "*":
        result = 1
        for n in numbers:
            result *= n
    else:
        result = numbers[0]
        for n in numbers[1:]:
            try:
                if op == "-":
                    result -= n
                elif op == "/":
                    result /= n
                elif op == "//":
                    result //= n
                elif op == "%":
                    result %= n
                elif op == "**":
                    result **= n
            except ZeroDivisionError:
                print("Error: division by zero")
                return

    print("Result:", result)

if __name__ == "__main__":
    main()
```

Notes and recommendations
-------------------------
- If you only intend to work with integers, use `int` instead of `float`. Be careful with `//` (integer floor division) behavior with negative numbers.
- For `**` (exponentiation), applying it left-to-right like `(((a ** b) ** c) ...)` can quickly produce very large numbers; consider restricting or warning the user.
- Add unit tests for expected behaviors to prevent regressions.
- Improve prompts and add a `--help` or CLI arguments if you want non-interactive use (for scripting).

License & Author
----------------
- This README and the suggested fixes are provided as guidance. Keep or adapt them as needed.
- Original script author: repository owner (see repo for details).
