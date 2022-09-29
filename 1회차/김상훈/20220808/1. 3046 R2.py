import sys
sys.stdin = open("1.R2.txt", "r")


R1 , S = map(int,input().split())
R2 = S*2 - R1 
print(R2)


# 숫자1 + 숫자2 / 더한숫자갯수 = 평균

# 숫자2 = 평균 x 더한숫자갯수 - 숫자1