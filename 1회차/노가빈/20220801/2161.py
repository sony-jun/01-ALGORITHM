num = int(input())

if num >=1 and num <= 1000:

    card = []
    removeCard=[]

    for i in range(num):
        card.append(i+1)

    for i in range(num-1): # 인덱스에러 발생하지 않게 num-1까지로 제한
        removeCard.append(card[0]) #카드를 버린다
        del card[0]
        card.append(card[0]) # 카드를 맨뒷장으로 옮긴다_1
        del card[0] # 카드를 맨뒷장으로 옮긴다_2

    resultList = removeCard + card

    for i in resultList:
        print(i, end=' ')

else:
    print('1~1000 안에서 다시 입력해주세요')