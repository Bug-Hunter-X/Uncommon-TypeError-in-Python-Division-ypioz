def function_with_uncommon_error(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return float('inf')
    except TypeError:
        return None

# The uncommon error is when x is a string and y is not 0, which will lead to a TypeError. This error can be tricky to debug because it's not a common exception
print(function_with_uncommon_error(10, 0)) # Output: inf
print(function_with_uncommon_error(10, 2)) # Output: 5.0
print(function_with_uncommon_error("10", 2)) # Output: None