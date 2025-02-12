#Built-in Math Functions
x = min(5, 10, 25)
y = max(5, 10, 25)
z = abs(-7.25)
a = pow(4, 3)

print(x)
print(y)
print(z)


#Math module 
import math

x = math.sqrt(64)
z = math.ceil(1.4) # returns 2
y = math.floor(1.4) # returns 1
a = math.pi

print(x)
print(y)
print(z)
print(a)


#Lab Tasks 

#1
degree = float(input("Input degrees: "))
radian = degree*(math.pi/180)
print(radian)

#2
height = float(input("Height of trapezoid: "))
base_1 = float(input('Base one value: '))
base_2 = float(input('Base two value: '))
area = ((base_1 + base_2) / 2) * height
print("Area is:", area)

#3
from math import tan, pi
n_sides = int(input("Input number of sides: "))
s_length = float(input("Input the length of a side: "))
p_area = n_sides * (s_length ** 2) / (4 * tan(pi / n_sides))
print("The area of the polygon is: ",p_area)

#4
base = float(input('Length of base: '))
height = float(input('Measurement of height: '))
area = base * height
print("Area is: ", area)