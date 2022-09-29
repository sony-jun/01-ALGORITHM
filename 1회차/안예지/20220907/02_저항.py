# 1076
"""
"""
import sys
sys.stdin = open("저항.txt")

colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

one = str(colors.index(input()))
two = str(colors.index(input()))
three = 10 ** colors.index(input())

print(int(one + two) * three)