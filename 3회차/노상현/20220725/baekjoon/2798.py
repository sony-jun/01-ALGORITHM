n,m = list(map(int, input().split(' ')))# 인풋이 두줄이기에 n,m 첫째 줄 cards 둘째 줄
cards = list(map(int, input().split(' '))) 

result = 0 # result, length 를 초기화
length = len(cards)

for i in range (0, length): # 3중 반복문으로 cards 의 합을 sum_value 에 저장한다. 
    for j in range(i+1, length): 
        for k in range (j+1, length):
            sum_value = cards[i]+cards[j]+cards[k]
            if sum_value <=m:   # 문제에서 m 보다 세 개의 카드의 합이 작아야 하는 조건이 있기 떄문에 if 문을 사용하고
                result = max(result, sum_value) #result 에 이들의 최대값을 저장하고 출력한다.
print(result)
