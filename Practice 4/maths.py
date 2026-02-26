import math
import random
# 1
deg = float(input())
rad = deg * (math.pi / 180)
print(f"Radian: {rad}")

# 2
h = float(input())
b1 = float(input())
b2 = float(input())
area = (b1 + b2) / 2 * h
print(f"Area = {area}")

# 3
n = int(input())
s = float(input())
area = (n * s * s) / (4 * math.tan(math.pi / n))
print(f"The area of the polygon = {area}")

# 4
base = float(input())
h = float(input())

area = base * h
print(f"Area = {area}")

# 5
print("Random float:", random.random())
print("Random int:", random.randint(1, 10))

choices = ["apple", "banana", "cherry"]
print("Random choice:", random.choice(choices))

random.shuffle(choices)
print("Shuffled list:", choices)