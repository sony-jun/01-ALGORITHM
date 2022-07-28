import sys
sys.stdin = open('input.txt')

N = int(input())
card_dic = {}

for i in range(N):
    a = input()
    card_dic[a] = card_dic.get(a , 0) + 1

lst = sorted([k for k,v in card_dic.items() if max(card_dic.values()) == v])
print(lst[0])