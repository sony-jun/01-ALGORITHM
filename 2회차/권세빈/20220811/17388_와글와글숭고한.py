import sys
sys.stdin = open('17388.txt', 'r')

a = list(map(int,input().split()))
b = ['Soongsil', 'Korea','Hanyang']

if sum(a) >= 100:
    print('OK')

else:
    print(b[a.index(min(a))])