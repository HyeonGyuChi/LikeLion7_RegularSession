''' # by HyeonGyu
3.(If/else) Given an integer, print "odd" if it's odd and print "even" otherwise.

- Example input: 5
- Example output: add '''

num = int(input('Input Integer : '))
if num%2 == 0 :
    str = "even"

else :
    str = "odd"

print("{} is {}".format(num, str))
