# n , m = 4, 2
# stk1 = 2
# stack1 = [3, 1]
# stk2 = 2
# stack2 = [4, 2]

chk = True #번호수 나열이 가능한지 아닌지 확인하기 위한 변수
n, m = map(int, input().split())
# n: 교과서의 총 수, m: 교과서의 더미 개수 > 이 개수 만큼 반복문을 돌려야 함... 각 더미 별로 확인

for _ in range(m):
    i = int(input()) #각 교과서 더미에 쌓인 교과서 수
    k = list(map(int, input().split())) #해당 교과서 더미 내 밑에서부터의 교과서 번호 공백으로 구분되어 입력
    for j in range(i - 1):
        # 각 더미 내의 책들의 정렬 순서 확인... 
        if k[j] < k[j + 1]:
            #한 더미라도 내림차가 아니면 순서대로 정렬할 수 없으므로 check를 False로 변경 후 반복문 탈출
            chk = False
            break
    # if not chk: break
print('Yes' if chk else 'No')


#pop끼리 모았을때 순서정렬이 되나..? 체크... 순서대로 pop한거 저장해서 1234 순 인지 확인해보는 걸로 다시 짜보자
