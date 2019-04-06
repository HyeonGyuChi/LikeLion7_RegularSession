''' # by HyeonGyu
9. Given a string in which the letter h occurs at least twice. Remove from that string the first and the last occurrence of the letter h, as well as all the characters between them.

- Example input: In the hole in the ground there lived a hobbit
- Example output: In tobbit
'''

str = input("String : ")
print("Refind : ", str[:str.find('h')], str[str.rfind('h')+1:], sep = '')