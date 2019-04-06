''' # by HyeonGyu
5.(For) Given two integers A and B (A ≤ B). Print all numbers from A to B inclusively.

- Example input: 1 10
- Example output: 1 2 3 4 5 6 7 8 9 10
'''

start, end = map(int, input("Input Start End Integer : ").split())

if start > end :
    print("Error < You should input to this form : [Start ≤ End] >")

else :
    print("Output : ", end = " ")
    for num in range(start, end+1) :
        print(num, end = " ")

