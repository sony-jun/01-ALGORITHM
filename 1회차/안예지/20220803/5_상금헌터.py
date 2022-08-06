# 15953.
"""
"""
import sys
sys.stdin = open("상금헌터.txt")

score_dict = {1: 500, 3: 300, 6: 200, 10: 50, 15: 30, 21: 10}
score_dict2 = {1: 512, 3: 256, 7: 128, 15: 64, 31: 32}
# keys_sum = 1
# keys_sum2 = 1
# for i in range(N):
#     score_dict[keys_sum + i] = int(input())
    # i += 1
    # keys_sum += i
# print(score_dict)
# for i in range(5):
#     score_dict2[keys_sum2 + i] = int(input())
# print(score_dict2)
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    if a <= 21:
        for key in score_dict:
            if key >= a:
                key1 = score_dict[key]
                break
    else:
        a == 0
        
    if b <= 31:
        for key in score_dict2:
            if key >= b:
                key2 = score_dict2[key]
                break
    else:
        b == 0
    print(f'{key1 + key2}' + '0000')
    
    
    