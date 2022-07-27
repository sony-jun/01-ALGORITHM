# 리스트에 튜플로 받는다
# 등수 리스트 제작
# 각자의 등수 기본값은 1로 설정
# 0번 인덱스 사람부터 나머지 사람과 비교하여 이기면 상대방이 1등수 추가 본인은 유지
# 지면 상대방은 유지 본인은 1등수 추가
# 1번 인덱스 사람은 앞에 사람과는 비교 했으니 뒤에만 비교
# 반복
# 등수 리스트 출력

students = int(input())                     # t는 전체 학생수
rank_lst = [1]*students                     # 순위 리스트 [1,1,1,1,1]
info_lst = []                               # 정보 리스트 [[75,180],[68,175],...]

for i in range(students):                   # t번 정보 입력
    w, h = map(int,input().split())
    info_lst.append([w,h])

for idx in range(students-1):               # idx는 0부터 students-2 까지 순회. 마지막 학생은 제외
    [w1, h1] = info_lst[idx]                # 첫 번째 학생. idx 인덱스의 info_lst불러옴

    for idx_2 in range(idx+1,students):     # i는 idx 다음의 인덱스 부터 끝까지(students-1). 첫번째 학생은 제외
        [w2, h2] = info_lst[idx_2]          # 두 번째 학생.
            
        if w1 > w2 and h1 > h2:         # 둘 다 크거나 하나만 큰 경우
            rank_lst[idx_2] += 1
        elif w1 < w2 and h1 < h2:         # 둘 다 작거나 하나만 작은 경우
            rank_lst[idx] += 1

for i in rank_lst:         # 순위 출력
    print(i,end=" ")