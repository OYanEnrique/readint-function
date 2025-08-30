# 🛡️ Safe Integer Input Function (readint)

A script that demonstrates a highly reusable and robust utility function, `readint()`. This function is designed to safely get an integer from the user, handling errors and re-prompting until valid input is received.

## Features

* **Input Validation**: Uses a `while True` loop and the `.isnumeric()` method to reject any non-numeric input.
* **Error Messaging**: Provides clear feedback to the user when they enter invalid data.
* **Reusable**: Designed to be imported and used in any other program that needs to reliably read an integer from the console.
* **Well-Documented**: Includes a professional docstring explaining its purpose, arguments, and return value.

## How to Use

1.  Ensure you have Python installed.
2.  Save the code as a `.py` file (e.g., `readint_function.py`).
3.  Run the script from your terminal:
    ```sh
    python readint_function.py
    ```
4.  The script will prompt you to enter a number. Try entering text first to see the error message, then enter a valid number.

### Example Session

```sh
> python readint_function.py
Enter a number:
abc
Error, enter a valid number!
Enter a number:
10
You entered the number 10
```

### Using in other projects

To use this function, you can import it into another script and call it with your desired prompt message:

```python
from readint_function import readint

age = readint('Please enter your age: ')
print(f'You are {age} years old.')
```
