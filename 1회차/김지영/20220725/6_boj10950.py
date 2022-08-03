T = int(input())
r = []
# test_case돌때마다 출력하는게 아니라 출력을 한번에 뱉어야하네요.
# 빈 리스트를 만들고 result를 집어넣어 리스트가 다 완성된 후 출력해줍시다.
# 입력값의 seperater는 split함수 안에 넣기
for test_case in range(T):
    A, B = map(int, input().split())
    result = A + B
    r.append(result)
for i in r:
    print(i)