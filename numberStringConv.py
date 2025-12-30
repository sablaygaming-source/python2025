# Convert string to number with high sensitivity
def string_to_number(s):
    """Convert string to int or float with strict validation"""
    # Remove leading/trailing whitespace
    s = s.strip()
    
    # Check if string is empty
    if not s:
        return "Error: Empty string is not a valid number"
    
    # Check if string contains any letters or invalid characters
    # Valid characters: digits, decimal point, minus/plus sign
    valid_chars = set('0123456789.-+')
    if not all(c in valid_chars for c in s):
        return f"Error: '{s}' is not a valid number (contains invalid characters)"
    
    try:
        # Try converting to int first (if no decimal point)
        if '.' not in s:
            result = int(s)
        else:
            # Convert to float if it has a decimal point
            result = float(s)
        return result
    except ValueError:
        return f"Error: '{s}' is not a valid number"

# Convert number to string
def number_to_string(n):
    """Convert int or float to string"""
    if isinstance(n, (int, float)):
        return str(n)
    else:
        return f"Error: {n} is not a number (type: {type(n).__name__})"

# Test cases with high sensitivity
print("=== String to Number (High Sensitivity) ===")
test_strings = [
    "123",       # Valid
    "45.67",     # Valid
    "-100",      # Valid
    "+50",       # Valid
    "-.",      # Invalid - starts with letter
    "-.123a",      # Invalid - ends with letter
    "12a34",     # Invalid - letter in middle
    "abc",       # Invalid - all letters
    "12.34.56",  # Invalid - multiple decimals
    "",          # Invalid - empty
    "  89  ",    # Valid - whitespace trimmed
    "3.14159",   # Valid
]

for test in test_strings:
    result = string_to_number(test)
    status = "✓" if isinstance(result, (int, float)) else "✗"
    print(f"{status} '{test}' -> {result}")

print("\n=== Number to String ===")
test_numbers = [
    100,
    -50.5,
    0,
    3.14159,
    "not_a_number",  # Invalid input
]

for test in test_numbers:
    result = number_to_string(test)
    status = "✓" if isinstance(result, str) and "Error" not in result else "✗"
    print(f"{status} {test} -> '{result}'")

# Additional edge case testing
print("\n=== Edge Cases ===")
edge_cases = [
    "123abc456",  # Mixed
    "12 34",      # Space in middle
    "1.2.3",      # Multiple dots
    "--5",        # Double minus
    "5-",         # Minus at end
]

for test in edge_cases:
    result = string_to_number(test)
    print(f"'{test}' -> {result}")

################################################3
# another
