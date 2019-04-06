''' # by HyeonGyu
14. Given a list of numbers, count a number of pairs of equal elements. Any two elements that are equal to each other should be counted exactly once.

- Example input1: 1 2 3 2 3
- Example output1: 2
- Example input2: 1 1 1 1 1
- Example output2: 10
'''

# 1. 각각 원소들의 개수를 check > countElement {'원소': 개수}
# 2. 2개이상인 원소들 추리기
# 3. 그러한 원소들에 각각 원순열 공식 적용 > n개가 있을 때 그중 r개를 골라 짝을 만들수 있는 모든 경우의 수(중복한짝없이)
# CircularPermutationm(n,r) > ( n! / n-r! ) / 2
# 4.각각의 원소들의 원순열을 구한 후 모두 더함



def Factorial(n) : # n!
    fac = 1

    if n <= 1 :
        return fac
    else :
        for i in range(1, n+1) :
            fac = i*fac
        return fac

# n개가 있을 때 그중 r개를 골라 짝을 만들수 있는 모든 경우의 수(중복한짝없이)
def CircularPermutation(n,r) : # 원순열 공식 ( n! / n-r! ) / 2
    return ( Factorial(n) /  Factorial(n-r) ) / 2


strList = input().split()
countElement = {}
case = 0 # output == 짝질수있는 모든경우의 수

# numList 각각 원소들의 개수파악
for num in strList :
    if num in countElement :
        countElement[num] += 1
    else :
        countElement[num] = 1

# 2개이상은 원소들만 접근 후 그 원소의 case(모든경우의수)를 모두 더함
for key, value in countElement.items():
    if value >= 2 : # 2개이상 원소
        case += CircularPermutation(value, 2)
    else :
        pass

print("case :", int(case))


