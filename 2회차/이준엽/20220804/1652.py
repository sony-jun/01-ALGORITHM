n = int(input())
room = [list(input()) for i in range(n)]
line = 0
column = 0

for i in range(n):
    l = 0
    for j in range(n):
        if room[i][j] == '.':
            l+=1
        else:
            l=0
        if l == 2:
            line+=1

for j in range(n):
    c = 0
    for i in range(n):
        if room[i][j] == '.':
            c+=1
        else:
            c=0
        if c == 2:
            column+=1
print(line,column)
       
