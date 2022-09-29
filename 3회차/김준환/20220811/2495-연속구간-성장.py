input_lst = []
cnt_lst = [[0],[0],[0]]
i = 0
for _ in range(3):
    input_lst.append(input())
for text in input_lst:
    cnt = 1
    before = '?'
    d = 0
    for t in text:
        d += 1
        if t == before:
            cnt += 1
            if d == len(text):
                cnt_lst.append(cnt)
                break
        else:
            cnt_lst[i].append(cnt)
            cnt = 1
            before = t
    i += 1
for m in cnt_lst:
    print(max(m))