''' # by HyeonGyu
12. Fibonacci index
Fibonacci numbers are the numbers in the integer sequence starting with 1, 1 where every number after the first two is the sum of the two preceding ones:

1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Given a positive integer, determine if it's the nth Fibonacci number for some n. If it is, print such n, otherwise print -1.

- Example input: 8
- Example output: 6
'''

num = int(input("Input integer : "))
index = 0

if num == 1 :
    index = (1, 2)

else :

    a1 = 1
    a2 = 1

    index = 2

    while True :

        a3 = a1 + a2
        index += 1

        if num == a3 :
            break

        elif num < a3 :
            index = -1
            break

        else :
            a1, a2 = a2, a3


print("Ouput Integer : ", index)