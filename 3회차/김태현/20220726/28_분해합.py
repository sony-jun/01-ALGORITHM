
import sys
sys.stdin = open("28_분해합.txt", "r")
N = int(input())

#자릿수 구하기
def BHH(num):

    result = []
    cnt = 0

    while N:
        result.append(N % 10)
        N //= 10
        cnt += 1
    
    return cnt, result

