#1
def square(n):
    for i in range (1, n+1):
        yield i * i

N = int(input())
for num in square(N):
    print(num)

#2

def even_numbers(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i

n = int(input())

result = ""

for num in even_numbers(n):
    result += str(num) + ","

print(result[:-1])  

#3

def divisible_by_3_and_4(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


n = int(input("Enter n: "))

for num in divisible_by_3_and_4(n):
    print(num)

#4

def squares(a, b):
    for i in range(a, b + 1):
        yield i * i


a = int(input("Enter a: "))
b = int(input("Enter b: "))

for value in squares(a, b):
    print(value)

#5

def countdown(n):
    for i in range(n, -1, -1):
        yield i


n = int(input("Enter n: "))

for num in countdown(n):
    print(num)