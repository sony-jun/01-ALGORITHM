# 1302
"""
"""
import sys
sys.stdin = open("베스트셀러.txt")
# cubic_dict = {}
# for number in range(1, 4):
#     cubic_dict[number] = number ** 3
# print(cubic_dict)

# cubic_dict = {number : number ** 3 for number in range(1, 4)}
# print(cubic_dict)

book_dict = {}
for _ in range(int(input())):
    key = input()
    book_dict[key] = book_dict.get(key, 0) + 1
# print(book_dict) 

max_ = max(book_dict.values())
dis = list(book_dict.values()).count(max_)
maxes = []
for key in book_dict:
    if book_dict[key] == max_:
        maxes.append(key)
    
if dis >= 2:
    maxes = sorted(maxes)
    print(maxes[0])

else:
    print(maxes[0])