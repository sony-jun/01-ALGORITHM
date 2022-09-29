import sys
sys.stdin = open('03_input.txt')

fList = []

for _ in range(5):
    fList.append(input())

chk = False
for f in fList:
    if 'FBI' in f:
        print(fList.index(f)+1, end=' ')
        chk = True
if chk == False:
    print('HE GOT AWAY!')
