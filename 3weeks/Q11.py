''' # by HyeonGyu
11.(While) Fibonacci numbers
Fibonacci numbers are the numbers in the integer sequence starting with 1, 1 where every number after the first two is the sum of the two preceding ones:

1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Given a positive integer n, print the nth Fibonacci number.

- Example input: 6
- Example output: 8
'''
time = 0

num = int(input("Input Integer : "))

def fibonacci(index) :
    global time
    time += 1
    print("재귀회수:", time)

    if index <= 2 :
        return 1

    return fibonacci(index-1) + fibonacci(index-2)

print("Output : ", fibonacci(num))

time = 0
a1, a2 = [1]*2

for _  in range(2, num) :
    time += 1
    print("for문회수 :", time)

    a3 = a1 + a2
    a1, a2 = a2, a3


print("Answer:", a3)