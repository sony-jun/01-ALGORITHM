import sys                                  # 디스코드 자유-qa 참고
input = sys.stdin.readline                  # 입력 효율 차이

N, M = map(int, input().split())            # 교과서 수 N, 더미 수 M
possible = "Yes"                            # 초기값 가능 Yes

for i in range(1, M+1):                     # M개 중 i번째 더미
    k = int(input())                        # i번째 더미의 교과서 수 k
    ki = list(map(int, input().split()))    # k개의 교과서
    
    for idx in range(k-1):                  # i번째 더미가
        if ki[idx] < ki[idx+1]:             # 내림차순 정렬이 아니면
            possible = "No"                 # 불가능 No
            break

print(possible)                             # 가능 여부 출력