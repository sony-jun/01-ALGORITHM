import sys

sys.stdin = open("12_덩치.txt")

T = int(input())
rank_T = []
for i in range(T):
    x, y = map(int, input().split())
    rank_T.append((x, y)) # [(55, 185), (58, 183), (88, 186), (60, 175), (46, 155)]
for j in rank_T: #rank_T의 값을 j에 입력하면 rank_T[0]인 55,185는 각 j[0] j[1]로 저장된다.
    rank = 1
    for k in rank_T: # 0번 배열 값을 0번을 제외한 나머지 값과 2중 for문을 이용하여 전체 순회하며 비교한다.
        if j[0] < k[0] and j[1] < k[1]: 
                rank += 1 # 비교하여 j 리스트가 더 작으면 rank +1 로 낮아진다. 그 외의 결과는 인정하지 않는다.
    print(rank,end=" ")