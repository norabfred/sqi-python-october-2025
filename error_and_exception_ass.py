# 1. Define a custom exception called NegativeNumberError.
# Write a function check_positive(number) that raises 
# NegativeNumberError if the input number is negative.


class NegativeNumberError(Exception):
    pass

def check_positive(number):
    if number < 0:
         raise NegativeNumberError("Negative numbers are not allowed.")
    else:
        print(f"{number} is positive.")       

try:
    num = int(input("Enter a number: "))
    check_positive(num)

except NegativeNumberError as e:
    print(f"Error: {e}")

except ValueError:
    print("Please enter a valid number.")

# Catch the exception when calling the function.
# Handle Multiple Exceptions:
# Write a function safe_divide(a, b) that performs division.
# Handle ZeroDivisionError if the divisor is zero.
# Handle TypeError if the inputs are not numbers.
# Handle ValueError if the inputs are not convertible to floats.
# class HandleMultiple(Exception):
#     pass
def safe_divide(a, b):

    try:
        a = float(a)
        b = float(b)
    
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    
    except TypeError:
        return "Error: Inputs must be numbers."
    
    except ValueError:
        return "Error: Inputs must be convertible to floats."
print(safe_divide([5], 3))