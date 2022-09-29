text_ = input()
a = text_.upper()
result = list(a)
cnt = {}
for j in result:
    if j in cnt:
        cnt[j] += 1
    else:
        cnt[j] = 1

print('?') if len([k for k,v in cnt.items() if max(cnt.values()) == v]) > 1 else print(max(cnt, key=cnt.get))
