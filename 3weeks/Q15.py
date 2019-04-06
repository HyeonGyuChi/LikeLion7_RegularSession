''' # by HyeonGyu
15. (Dicts) The text is given in a single line. For each word of the text count the number of its occurrences before it.

- Example input : one two one two three two four three
- Example output: 0 0 1 1 0 2 0 1
'''

strList = "one two one two three two four three".split()

dict = {}

for word in strList :
    if word in dict :
        dict[word] += 1

    else :
        dict[word] = 0

    print(dict[word], end=" ")