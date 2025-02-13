import re
#1
def match_a_followed_by_zero_or_more_b(text):
    pattern = r'^ab*$'
    if re.search(pattern, text):
        return "Found a match!"
    else:
        return "Not matched!"

# Test
print(match_a_followed_by_zero_or_more_b("abbb"))   # Found a match!
print(match_a_followed_by_zero_or_more_b("a"))      # Found a match!
print(match_a_followed_by_zero_or_more_b("b"))      # Not matched!
print(match_a_followed_by_zero_or_more_b("abbbc"))  # Not matched!


#2
def match_a_followed_by_two_to_three_b(text):
    pattern = r'^ab{2,3}$'
    if re.search(pattern, text):
        return "Found a match!"
    else:
        return "Not matched!"

# Test
print(match_a_followed_by_two_to_three_b("abb"))   # Found a match!
print(match_a_followed_by_two_to_three_b("abbb"))  # Found a match!
print(match_a_followed_by_two_to_three_b("ab"))    # Not matched!
print(match_a_followed_by_two_to_three_b("abbbb")) # Not matched!


#3 
def find_lowercase_sequences_with_underscore(text):
    pattern = r'[a-z]+_[a-z]+'
    return re.findall(pattern, text)

# Test
sample_text = "hello_world test_example some_MixedCase not_valid"
print(find_lowercase_sequences_with_underscore(sample_text))
# Output: ['hello_world', 'test_example']

#4

def find_upper_followed_by_lower(text):
    pattern = r'[A-Z][a-z]+'
    return re.findall(pattern, text)

# Test
sample_text = "Hello World HELLO wOrld Python JAVA"
print(find_upper_followed_by_lower(sample_text))
# Output: ['Hello', 'World', 'Python']


#5
def match_a_anything_b(text):
    pattern = r'^a.*b$'
    if re.search(pattern, text):
        return "Found a match!"
    else:
        return "Not matched!"

# Test
print(match_a_anything_b("ab"))        # Found a match!
print(match_a_anything_b("a123b"))     # Found a match!
print(match_a_anything_b("acccb"))     # Found a match!
print(match_a_anything_b("abcxyz"))    # Not matched!

#6
def replace_space_comma_dot_with_colon(text):
    pattern = r'[ ,.]'
    return re.sub(pattern, ':', text)

# Test
sample_text = "Hello, world. This is a test"
print(replace_space_comma_dot_with_colon(sample_text))
# Output: "Hello:world:This:is:a:test"


#7 
def snake_to_camel(snake_str):
    """Converts snake_case to camelCase."""
    parts = snake_str.split('_')
    # Keep the first part as is (all lower), capitalize subsequent parts
    return parts[0].lower() + ''.join(word.capitalize() for word in parts[1:])

# Test
print(snake_to_camel("snake_case_example"))  # snakeCaseExample
print(snake_to_camel("test_string")) 