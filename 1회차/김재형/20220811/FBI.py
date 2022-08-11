import sys
sys.stdin = open('FBI_input.txt')

list_ = []
cnt = 0
for i in range(5):
    fbi = input()
    cnt += 1
    if 'FBI' in fbi:
        print(i+1, end=' ')
        list_.append(0)
if len(list_) == 0:
    print('HE GOT AWAY!')
