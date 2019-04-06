''' # by HyeonGyu
6. For the given integer N calculate the following sum:
1³ + 2³ + ... + N³

- Example input: 3 Example output: 36
'''

num = int(input("1³ + 2³ + ... + N³, N ? "))
sum = 0

for n in range(1, num+1) :
    sum += n**3

print("Answer :", sum)
