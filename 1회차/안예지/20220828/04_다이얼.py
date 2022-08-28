# 5622
"""
"""
import sys
sys.stdin = open("다이얼.txt")

phone = {'ABC' : 2,
         'DEF' : 3,
         'GHI' : 4,
         'JKL' : 5,
         'MNO' : 6,
         'PQRS' : 7,
         'TUV' : 8,
         'WXYZ' : 9
}
word = input()
time = 0
for idx in range(len(word)):
    for key in phone:
        if word[idx] in key:
            time += phone[key] + 1

print(time)