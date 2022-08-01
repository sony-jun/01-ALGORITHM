from sys import stdin

n = int(stdin.readline())
# 빈 딕셔너리 생성
dict = {}

for i in range(n):
    # name 입력 받기
    name = stdin.readline()
    # 딕셔너리에 name이 있으면
    if name in dict:
        # 딕셔너리 키의 name의 값에 1 증가
        dict[name] += 1
    # 딕셔너리에 name이 없으면
    else:
        # 딕셔너리 키의 name의 값에 1 저장
        dict[name] = 1

for i in range(n-1):
    # name 입력 받기
    name = stdin.readline()
    # 딕셔너리 키의 name 값이 1이면
    if dict[name] == 1:
        # 키 값 삭제
        del dict[name]
    # name이 딕셔너리에 있으면
    elif name in dict:
        # 딕셔너리 키의 name의 값에 1 감소
        dict[name] -= 1

# 남아있는 딕셔너리의 name 키 출력
print(*dict)