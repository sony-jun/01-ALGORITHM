# 1371.
""" 

"""
# import sys 
# sys.stdin = open("글자.txt")

# count_dict = {}
# # 최대 50줄
# words = input()
# while words != '':
#         words = input().split()
        
#         # 입력받는 값이 없으면 반복문을 빠져나온다.
#         for idx in range(len(words)):
#             for chr in words[idx]:
#                 count_dict[chr] = count_dict.get(chr, 0) + 1
                
# max_count = max(count_dict.values())
# for key in count_dict:
#     if count_dict[key] == max_count:
#         print(key)
        
import sys
# input = sys.stdin.read

count_dict = {}
words = input().rstrip()

for idx in range(len(words)):
    for chr in words[idx]:
        count_dict[chr] = count_dict.get(chr, 0) + 1
                
max_count = max(count_dict.values())
for key in count_dict:
    if count_dict[key] == max_count:
        print(key, end = "")