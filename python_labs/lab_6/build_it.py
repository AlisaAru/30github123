import math

def multiply_list(numbers):
    return math.prod(numbers)

# Example usage:
nums = [2, 3, 4, 5]
result = multiply_list(nums)
print(f"The product of {nums} is {result}")


# 2. Count the number of uppercase and lowercase letters in a string
def count_upper_lower(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    return upper_count, lower_count

# Example usage:
input_string = "Hello World!"
upper_case, lower_case = count_upper_lower(input_string)
print(f"Original String: {input_string}")
print(f"No. of Upper case characters : {upper_case}")
print(f"No. of Lower case characters : {lower_case}")


# 3. Check if a passed string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

# Example usage:
test_string = "racecar"
if is_palindrome(test_string):
    print(f'"{test_string}" is a palindrome.')
else:
    print(f'"{test_string}" is not a palindrome.')


# 4. Invoke square root function after specific milliseconds
import math
import threading

def schedule_sqrt():
    number = float(input("Введите число: "))
    delay_milliseconds = float(input("Введите задержку в миллисекундах: "))

    
    def compute_and_print_sqrt():
        result = math.sqrt(number)
        print(f"Квадратный корень числа {number} через {delay_milliseconds} мс -> {result}")

    # Конвертация миллисекунд в секунды
    delay_in_seconds = delay_milliseconds / 1000.0
    
    # Запускаем таймер
    timer = threading.Timer(delay_in_seconds, compute_and_print_sqrt)
    timer.start()

schedule_sqrt()


# 5. Check if all elements of the tuple are true
def all_true_in_tuple(tpl):
    return all(tpl)

# Example usage:
my_tuple = (True, 1, "Non-empty string")
result = all_true_in_tuple(my_tuple)
print(f"Are all elements of {my_tuple} true? {result}")

# Another example:
my_tuple2 = (True, 1, "")
result2 = all_true_in_tuple(my_tuple2)
print(f"Are all elements of {my_tuple2} true? {result2}")


# sorted() with a Custom Key Function
# We have a list of tuples (name, score)
players = [
    ("Alice", 50),
    ("Bob", 120),
    ("Charlie", 75),
    ("Diana", 120),
    ("Eve", 50)
]

# Sort primarily by score (descending), then by name (ascending)
sorted_players = sorted(players, key=lambda x: (-x[1], x[0]))

print("Sorted players:", sorted_players)


#enumerate() with a Custom Start Index

fruits = ["apple", "banana", "cherry"]

# Start counting from 1
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

# whare is my contripution?