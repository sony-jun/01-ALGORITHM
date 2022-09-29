# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

A = int(input())
B = int(input())
C = int(input())

mul = A * B * C
# print(mul) 17037300
mul_str = str(mul)
ls = []
count = {}
for i in mul_str:
    ls.append(i)
# print(ls)
for j in range(10):
    count[j] = 0
    #print(count)
for num in ls:
    count[int(num)] += 1
for key, val in count.items():
    print(val)


#===================================
    
# A = int(input())
# B = int(input())
# C = int(input())

# mul = A * B * C
# # print(mul) 17037300
# mul_str = str(mul)
# for i in range(10):
# 	print(mul_str.count(str(i)))

#================================

# #mul값을 str로 변환
# #딕셔너리 키값에 삽입
# #밸류에 갯수 삽입
# #밸류 출력
# A = int(input())
# B = int(input())
# C = int(input())

# mul = A*B*C #17037300
# str_mul = str(mul)
# dict_mul = {}

# for num in range(10):
#     dict_mul[num] = 0
# #print(dict_mul) {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
# for i in str_mul:
#     dict_mul[int(i)] += 1
# #print(dict_mul) {0: 3, 1: 1, 2: 0, 3: 2, 4: 0, 5: 0, 6: 0, 7: 2, 8: 0, 9: 0}
# for val in dict_mul.values():
#     print(val)