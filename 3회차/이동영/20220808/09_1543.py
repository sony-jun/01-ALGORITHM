n = input()
m = input()
cnt = 0
for _ in range(len(n)):
    if m in n :
        n = n.replace(m,'0')
        cnt = n.count('0')
    if m not in n:
        break
print(cnt)