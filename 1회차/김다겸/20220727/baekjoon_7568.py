# 학생 수 입력
n = int(input())
# student 리스트 생성
student = []

# n만큼 순회
for i in range(n):
    # x, y값을 정수형으로 변환해서 저장
    x, y = map(int, input().split())
    # student 리스트에 (x, y)를 추가
    student.append((x, y))

# student 리스트를 순회
for i in student:
    # rank는 1로 초기화
    rank = 1
    # student 리스트를 순회
    for j in student:
        # 만약 i의 첫번째 값이 j의 첫번째 값보다 작고
        # i의 두번째 값이 j의 두번째 값보다 작으면
        if i[0] < j[0] and i[1] < j[1]:
            # rank에 1씩 더함
            rank += 1
    # rank 값 출력
    print(rank, end=' ')