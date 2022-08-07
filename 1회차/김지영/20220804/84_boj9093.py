line = int(input())
for _ in range(line):
    s = list(map(str,input().split()))
    rev_s = []
    for rs in s:
        rs = rs[::-1]
        rev_s.append(rs)
    rev_s = ' '.join(rev_s)
    print(rev_s)