
import sys
sys.stdin = open("28_분해합.txt", "r")

N = int(input())

#1부터 N까지 분해합 탐색

for num in range(1, N):
    BHH = num + sum(map(int, str(num)))

    if BHH == N:
        print(BHH)
        break

else:
    print(0)
