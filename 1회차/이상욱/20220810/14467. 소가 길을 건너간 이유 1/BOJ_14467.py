import sys
sys.stdin = open('14467.txt')

n = int(input())                        # 관찰 횟수 n번
arr = {}                                # 소의 번호와 위치를 저장
count = 0                               # 소가 길을 건넌 횟수 저장

for i in range(n):                      # n번만큼 반복문
    a, b = map(int, input().split())    # 소의 번호, 움직인 위치
    if a not in arr:
        arr[a] = b                      # a가 딕셔너리에 없으면 a(key), b(value) 값을 저장
    else:                               
        if arr[a] != b:                 # a가 이미 딕셔너리에 있다면 b(value)가 같은지 판별
            count += 1                  # 다르면 길을 건넌 것이니까 cnt += 1
            arr[a] = b                  # 길을 건넌 것을 표시해주기 위해 b(value)를 다시 저장
                                        # 만약 같다면 길을 건너지 않은 것이므로 반복문으로 이동
print(count)                            # 건넌 횟수 출력