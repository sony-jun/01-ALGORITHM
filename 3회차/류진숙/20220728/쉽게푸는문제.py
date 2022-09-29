import sys

sys.stdin = open('쉽게푸는문제.txt')

ab_range = list(map(int, input().split()))

A = ab_range[0]
B = ab_range[1]

list_ = []
for i in range(1, B+1):
    if i:
        list_ += [i] * i

print(sum(list_[A-1 : B]))

# 76ms 

# 이 방법의 오류를 알겠음 문자열이라서 50 53 이렇게 넘어가면 5, 0, 5, 3 이렇게 인식해서 더하는 것
# ab_range = list(map(int, input().split()))

# A = ab_range[0]
# B = ab_range[1]

# list_ = []
# for i in range(1, B+1):
#     if i:
#         char = str(i)
#         char *= i
#     list_.append(char)

# arr = ''.join(list_)


# result = sum(map(int, arr[A-1:B]))
# print(result)
