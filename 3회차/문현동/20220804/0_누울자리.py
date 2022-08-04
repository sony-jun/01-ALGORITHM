import sys
sys.stdin = open("0_누울자리.txt", 'r')

room = []
row_bed = 0
column_bed = 0

N = int(sys.stdin.readline())

for _ in range(N):
    room.append(sys.stdin.readline().rstrip())

for row in room:
    space = 0 # X 이전까지의 빈공간
    for cell in row:
        if cell == '.':
            space += 1
        else:
            if space >= 2:
                row_bed += 1
                space = 0
            else:
                space = 0
                continue
    if space >= 2:
        row_bed += 1

for row in range(len(room)):
    space = 0
    for column in range(len(room[row])):
        if room[column][row] == '.':
            space += 1
        else:
            if space >= 2:
                column_bed += 1
                space = 0
            else:
                space = 0
                continue
    if space >= 2:
        column_bed += 1

print(row_bed, column_bed)