#Python iterators and generators
# https://habr.com/ru/articles/337314/


#1
def generate_squares(N):
    for i in range(1, N+1):
        yield i * i

# Example usage:
N = int(input("Enter a number N: "))
for square in generate_squares(N):
    print(square, end=" ")

#2
def even_numbers(n):
    for i in range(0, n+1, 2):  # start at 0, go till n, with a step of 2
        yield i

# Example usage:
n = int(input("Enter a number n: "))
even_nums = even_numbers(n)
print(", ".join(str(num) for num in even_nums))

#3
def divisible_by_3_and_4(n):
    for i in range(0, n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Example usage:
n = int(input("Enter a number n: "))
for num in divisible_by_3_and_4(n):
    print(num, end=" ")

#4
def squares(a, b):
    for i in range(a, b+1):
        yield i * i

# Example usage:
a = int(input("Enter the starting number a: "))
b = int(input("Enter the ending number b: "))
for square in squares(a, b):
    print(square, end=" ")

#5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

# Example usage:
n = int(input("Enter a number n: "))
for number in countdown(n):
    print(number, end=" ")

