''' # by HyeonGyu
8.(String) Given a string consisting of words separated by spaces. Determine how many words it has. To solve the problem, use the method count.

- Example input: Hello World
- Example output: 2
'''

str = input("Input String : ")
split = str.split()

print("Word Num : ", len(split))