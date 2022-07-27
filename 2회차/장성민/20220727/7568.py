# 사람수 입력, 리스트 생성
N = int(input())
li = []

# 각 사람의 무게/키 리스트로 할당
for i in range(N):
    wei, hei = map(int, input().split())
    li.append([wei, hei])

# 이중 for문을 이용해 자신을 포함한 요소들 모두 돌며 비교
for i in range(N):
    rank = 1
    for j in range(N):
        if (li[i][0] < li[j][0]) and (li[i][1] < li[j][1]):
            rank += 1

    # 각 rank를 한 줄로 띄어서 출력     
    print(rank, end = ' ')





