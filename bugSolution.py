def function_with_uncommon_error_solution(x, y):
    if not isinstance(x,(int,float)) or not isinstance(y,(int,float)):
        return None
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return float('inf')

# The improved function includes type checking to prevent TypeErrors
print(function_with_uncommon_error_solution(10, 0)) # Output: inf
print(function_with_uncommon_error_solution(10, 2)) # Output: 5.0
print(function_with_uncommon_error_solution("10", 2)) # Output: None
print(function_with_uncommon_error_solution(10, "2")) # Output: None