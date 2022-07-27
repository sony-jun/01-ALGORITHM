n = input().upper()
cnt = [0 for i in range(26)]

for i in n:
    cnt[ord(i)-65] += 1

max_ = max(cnt)

if cnt.count(max_) != 1:
    print('?')
else:
    print(chr(cnt.index(max_) + 65))
