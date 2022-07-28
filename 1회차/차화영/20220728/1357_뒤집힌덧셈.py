import sys
sys.stdin = open("1357.txt")

x, y = input().split()
sum_ = str(int(x[::-1]) + int(y[::-1])) #거꾸로 슬라이싱한 후, 뒤집은 값을 더해준다. 이 때, int로 형변환을 해야만 더할 수 있음.
print(int(sum_[::-1]))

# 다른 풀이
# a = set()

# for i in range(10):
#     a.add(int(input()) % 42)

# print(len(a))