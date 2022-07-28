import sys
sys.stdin = open("2941.txt")

word = input() # ddz=z=
abc = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in abc:
    word = word.replace(i, 'x')
    # print(word) -- ddz=z=, ddz=z=, dxz=, dxz=, dxz=, dxz=, dxz=, dxx
    # print(len(word)) -- 6 6 4 4 4 4 4 3
    # print 위치 주의!
print(len(word))