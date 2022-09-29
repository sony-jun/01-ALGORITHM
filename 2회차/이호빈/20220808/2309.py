from itertools import combinations
#입력값을 범위만큼 리스트에 담아주고
height = [int(input()) for _ in range(9)]
#오름차순 정렬을 하고
height.sort()

#combinations 함수를 사용해서 7명씩 받아준다
combination = list(combinations(height, 7))

#리스트를 돌면
for comb in combination:
    #해당 리스트의 합이 100이면
    if sum(comb) == 100:
        # 리스트 아무거나 출력이니까 해당리스트의 요소값을 출력하고 break를 해준다.
        for c in comb:
            print(c)
        break




