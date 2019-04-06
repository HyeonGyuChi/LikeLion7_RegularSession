''' # by HyeonGyu
13.(Lists) Given a list of numbers, find and print the elements that appear in it only once. Such elements should be printed in the order in which they occur in the original list.

- Example input: 4 3 5 2 5 1 3 5
- Example output: 4 2 1

'''

list = list(map(int, input("Input : ").split()))

first = []
twice = []

for num in list :
    if num in first :
        twice.append(num)

    else :
        first.append(num)

set(twice)

for dup in set(twice) :
    if dup in first :
        first.remove(dup)

print("Only Once Numbers <In order of input> : ", first)
