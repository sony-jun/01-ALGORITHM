import sys


sys.stdin = open("input.txt")

# 여덟 자리의 양의 정수가 주어질 때, 
# 그 안에서 연속하여 같은 숫자가 나오는 것이 없으면 1을 출력하고, 
# 있으면 같은 숫자가 연속해서 나오는 구간 중 가장 긴 것의 길이를 출력하는 프로그램을 작성하라. 


for _ in range(3):
    N = list(map(int, input().split()))
    cnt = 0
    for i in range(len(N)):
        num = N[i]