def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

def multiply(a, b):
    return a * b
result = multiply(4, 7)
print(f"The product is: {result}")

# Function with a return value
def UnknownFunction(*Name):
    print(Name)
UnknownFunction("Alice", "Bob", "Charlie")

# Function with variable number of arguments
def UnknownFunctionWithKeywordArgs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
UnknownFunctionWithKeywordArgs(name="Alice", age=30, city="New York")

# Keyword arguments in functions
def add_numbers(Name,Age):
    print(f"Name: {Name}, Age: {Age}")
add_numbers(Name="Alice", Age=30)
 
# Default arguments in functions
def add_numbers_with_default(Name, Age=25):
    print(f"Name: {Name}, Age: {Age}")
add_numbers_with_default(Name="Bob")
add_numbers_with_default(Name="Charlie", Age=35)


# Lambda function example
square = lambda x: x * x
print(f"The square of 5 is: {square(5)}")

# lamada function with function as an argument

def apply_function(func, value):
    return func(value)
result = apply_function(square, 10)
print(f"The result of applying the square function to 10 is: {result}")


# Function with a docstring
def example_function():
    """This function does nothing."""
    pass
print(example_function.__doc__)