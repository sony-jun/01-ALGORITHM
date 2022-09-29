# https://www.acmicpc.net/problem/2577
import sys
sys.stdin = open("0_숫자의개수.txt")

a = int(input())
b = int(input())
c = int(input())
# 곱한 값 문자열 리스트로
result = list(str(a * b * c))
# 0~9까지 카운트 할 빈 리스트 
# num_list = [0] * 10
# # print(num_list, result) 중간체크

# # 리스트[int()]로 하면 그 숫자 자리 인덱스에 +1씩 카운트 없으면 그대로 0. 
# for num in result:
#     num_list[int(num)] += 1
    
# # 카운트 한 숫자리스트 프린트
# for nums in num_list:
#     print(nums)
    
for i in range(10): # 재우님
    print(result.count(str(i)))

# for i in range(10): 예린님
#     cnt = 0
#     for j in multiple:
#         if str(i) == j:
#             cnt += 1
#     print(cnt)