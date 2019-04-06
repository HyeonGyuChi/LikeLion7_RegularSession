''' # by HyeonGyu
4. Write a program that solves a linear equation ax = b in integers. Given two integers a and b (a may be zero),
print a single integer root if it exists and print "no solution" or "many solutions" otherwise.

- Example input 1: 1 -2 Example output 1:  -2
- Example input 2: 2 -1 Example output 2: no solution

'''

# a == 0  && b == 0 : x = many soultion
# a > 0 || a < 0 (a != 0) : x = b/a
# a == 0 && b != 0 : x = no solution

# 파이썬 한줄로 여러게 입력받기
a,b = map(float, input("Input a, b : ").split())


if a == 0 :
    if b == 0 :
        x  = "many soultion"
    else :
        x = "no solution"

else :
    if b == 0 :
        x = "0"
    else :
        x = b/a

print("x = ", x)
