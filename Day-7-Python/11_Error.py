# Types of Errors in Python | How to deal with them
# In Python, errors can be broadly categorized into several types. Understanding these errors helps in debugging and writing better code.
# Here are some common types of errors in Python:

# 1. Syntax Error
# Syntax errors occur when the code is not written correctly according to Python's syntax rules.
# Example:
def example_function():
    print("This will cause a syntax error")
    # example_function(  # Uncommenting this line will raise a SyntaxError
    
# 2. Runtime Error
# Runtime errors occur when the code is syntactically correct but fails during execution.
# Example:
def divide_by_zero():
    return 1 / 0  # This will raise a ZeroDivisionError

# 3. Logical Error
# Logical errors occur when the code runs without crashing but produces incorrect results.
# Example:
def logical_error_example():
    return 2 + 2  # This is logically correct, but let's say we expected 5

# 4. Indentation Error
def indentation_error_example():
    print("This is correct")
    # print("This will cause an indentation error")  # Uncommenting this line will raise an IndentationError

# 5. Name Error
def name_error_example():
    print(undefined_variable)  # This will raise a NameError

# 6. Type Error
def type_error_example():
    return "string" + 5  # This will raise a TypeError

# 7. Index Error
def index_error_example():
    my_list = [1, 2, 3]
    return my_list[5]  # This will raise an IndexError

# 8. Key Error
def key_error_example():
    my_dict = {'a': 1, 'b': 2}
    return my_dict['c']  # This will raise a KeyError
# 9. Value Error
def value_error_example():
    return int("not a number")  # This will raise a ValueError
    
# 10. Attribute Error
def attribute_error_example():
    my_list = [1, 2, 3]
    return my_list.non_existent_method()  # This will raise an AttributeError

# 11. Import Error
def import_error_example():
    import non_existent_module  # This will raise an ImportError

# 12. ZeroDivision Error
def zero_division_error_example():
    return 1 / 0  # This will raise a ZeroDivisionError

# 13. File Not Found Error
def file_not_found_error_example():
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
    return content