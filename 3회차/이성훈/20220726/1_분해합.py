# https://www.acmicpc.net/problem/2231
import sys

sys.stdin = open("1_분해합.txt")

N = int(input())

result_N = 0                    # # 결과 값 초기화
for i in range (1,N+1):
    list_N = map(int,str(i))    # 뭉쳐 있는 i값을 하나 하나 분해
    result_N = sum(list_N) + i  # i[0]부터 i[2]까지 값을 더하고 i값을 더함
    if result_N == N:           # 더한 값과 N값을 비교
        print(i)                
        break
else:
    print(0)

    





    
