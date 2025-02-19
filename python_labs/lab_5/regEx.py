import re
#1
def match_a_followed_by_b(string):
    pattern = r'.*a+b*.*'
    return re.fullmatch(pattern, string)

def match_a_followed_by_two_to_three_b(string):
    pattern = r'.*a(bb|bbb).*'
    return re.fullmatch(pattern, string) is not None

# Test cases
strings = ["gab", "ab", "tdbr", "abb", "arbbb", "abbbb", "b", "aaaabbb"]

print("Matching 'a' followed by zero or more 'b's:")
for s in strings:
    if match_a_followed_by_b(s):
        print(s)

print("\nMatching 'a' followed by two to three 'b's:")
for s in strings:
    if match_a_followed_by_two_to_three_b(s):
        print(s)


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


# #7 
def snake_to_camel(snake_str):
    return re.sub(r'_([a-z])', lambda match: match.group(1).upper(), snake_str)

# Test cases
snake_strings = ["hello_world", "convert_this_string", "snake_case_example", "python_is_fun"]

print("Snake case to camel case:")
for s in snake_strings:
    print(f"{s} -> {snake_to_camel(s)}")


# # #8 
# # def split_at_uppercase(text):
# #     # This will split at positions where there's an uppercase letter,
# #     # but keep the uppercase letter in the result.
# #     return re.split(r'(?=[A-Z])', text)

# # # Test
# # sample_text = "HelloWorldExample"
# # print(split_at_uppercase(sample_text))


# # #9
# # def insert_spaces_before_capital(text):
# #     # Insert space before any capital letter that is not at the start of the string
# #     return re.sub(r'(?<!^)(?=[A-Z])', ' ', text)

# # # Test
# # sample_text = "HelloWorldExample"
# # print(insert_spaces_before_capital(sample_text))


# # #10
# # def camel_to_snake(camel_str):
# #     # Insert an underscore before any uppercase letter that is not at the start
# #     snake = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str)
# #     return snake.lower()

# # # Test
# # print(camel_to_snake("camelCaseExample"))  # camel_case_example
# # print(camel_to_snake("CamelCaseExample"))  