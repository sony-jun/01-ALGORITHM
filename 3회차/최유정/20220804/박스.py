T = int(input())
for t in range(T):
    m, n = map(int, input().split())
    box = []
    new_box = [[0]*n for _ in range(m)]
    box_lst = []
    for i in range(m):
        box.append(list(map(int, input().split())))
    #열 순회 하면서 1 count
    for i in range(n):
        cnt = 0
        
        for j in range(m):
            if box[j][i] == 1:
                cnt += 1
                new_box[m-cnt][i] = 1 
                box_lst.append((j))


    new_lst = []
    for i in range(n):
        for j in range(m):
            if new_box[j][i] == 1:
                new_lst.append((j)) 

    print(sum([new_lst[i]-box_lst[i] for i in range(len(new_lst))]))

