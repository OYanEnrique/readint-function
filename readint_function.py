# Read Int function

def readint(msg):
	"""Reads a valid integer from the user and returns it.

    The function prompts the user with a message and continues to do so
    until a valid integer is entered. It displays an error message for
    non-numeric input.

    Args:
        msg (str): The message to display when prompting for input.

    Returns:
        int: The validated integer number entered by the user.
    """
	while True:
		enter = input(msg)
		if enter.isnumeric():
			enter = int(enter)
			return enter
		else:
			print('Error, enter a valid number!')
			
n = readint('Enter a number:')
print(f'You entered the number {n}')

help(readint)