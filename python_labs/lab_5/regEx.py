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