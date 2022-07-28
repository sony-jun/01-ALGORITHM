row = []
[row.append(i) for i in range(46) for j in range(i)] # 메모리에 올려놓음       
A, B = map(int, input().split()) # 입력
print(sum(row[A-1:B])) # 출력


# row = []
# for i in range(0, 46):
#     for j in range(i):
#         row.append(i)