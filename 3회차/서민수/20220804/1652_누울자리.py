# 문제를 읽고 이해한다

# 방은 N X N 으로 2차원 배열을 생성
# 연속해서 2칸이상 빈칸이 있으면 누울 수 있다
# 가로 세로 따로 알아야 함

# 프로그램 구현
lst_ = []
r, c = 0, 0
n = int(input())


for x in range(n):
    array = list(input())   
    lst_.append(array)
   # 행열 만들기
for x in range(n):
    #"."을 확인하기위한 cnt 변수
    cnt = 0
    for y in range(n):
        # lst_0.0 부터 순회해서 .을 찾는다
        if lst_[x][y] == '.':
            # .을 찾을 때마다 cnt 1씩증가
            cnt += 1
        else:
            # 그렇지 않다면 0으로 초기화
            cnt = 0
            # 누울자리가 2이상이면 누울 수 있기에  cnt가 2가되면
        if cnt == 2:
            # r에 1씩증가
            r +=1
for y in range(n):
    cnt = 0
    # 인덱스를 뒤어 . 이가 나올때
    if lst_[y][x] == '.':
        # cnt 변수에 1씩증가
        cnt +=1
    else:
        # 아니라면 0으로 초기화
        cnt = 0
        # 만약 cnt가 2가되면 
    if cnt == 2 :
        # c를 1씩 증가시켜라
        c += 1
print(r,c)
