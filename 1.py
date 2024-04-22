# Обработка ValueError
def string_to_int(s):
    try:
        return int(s)
    except ValueError:
        return "Error: Invalid input. Please provide a valid integer."

# Обработка FileNotFoundError, IOError
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: File '{filename}; not found."
    except IOError:
        return f"Error: Input/Output error while reading the file '{filename}'."

# Обработка ZeroDivisionError, TypeError return a / b
def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero."
    except TypeError:
        return "Error: Invalid type for division operation."

# Обработка IndexError, TypeError return lst(index)
def access_list_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return f"Error: Index our of range."
    except TypeError:
        return "Error: Invalid type for list indexing."