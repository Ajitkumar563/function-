def find_lower_upper(s):
    lower_chars = []
    upper_chars = []
    
    for char in s:
        if char.islower():
            lower_chars.append(char)
        elif char.isupper():
            upper_chars.append(char)
    
    return lower_chars, upper_chars

# Example usage
input_string = "Hello World!"
lower, upper = find_lower_upper(input_string)
print("Lowercase characters:", lower)
print("Uppercase characters:", upper)
