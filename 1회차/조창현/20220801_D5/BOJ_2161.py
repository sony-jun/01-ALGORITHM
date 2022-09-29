#card_list = [1, 2, 3, 4, 5, 6, 7]
## 인풋으로 숫자를 받아 들인다.
n = int(input())

## 비어있는 리스트를 초기화하고
card_list = []

for i in range(1, n + 1):
    ## 1부터 순서대로 숫자를 append 해준다.
    card_list.append(i)
    ## 리스트의 길이가 1이 될때까지 돌린다.

while len(card_list) > 1:
    ## 가장 첫번째 인덱스의 값을 pop 해주고
    ## [0] == 1
    print(card_list.pop(0), end = ' ')
    #print(card_list)
    ## 그 다음 인덱스의 값을 맨 뒤고 append 해준다.
    ## [0] == 2
    card_list.append(card_list.pop(0))
    #print(card_list)

print(card_list[0])