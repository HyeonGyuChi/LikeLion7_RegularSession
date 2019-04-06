''' # by HyeonGyu
7. There was a set of cards with numbers from 1 to N. One of the card is now lost. Determine the number on that lost card given the numbers for the remaining cards.
Given a number N, followed by N − 1 integers representing the numbers on the remaining cards (distinct integers in the range from 1 to N). Find and print the number on the lost card.

- Example input: 5 3 5 2 1
- Example output: 4
'''

cardNum = int(input("card Num : "))
cardList = list(range(1,cardNum+1))

for _ in range(cardNum-1) :
    while True :
        pick = int(input("Which card do you have ? : "))
        if pick in cardList:
            cardList.remove(pick)
            break
        else :
            print("Wrong select : you already selected or Boundary Exception ")
            continue



print("It's your LostCard : ", cardList)
