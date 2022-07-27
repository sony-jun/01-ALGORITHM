n = input()
word = n.upper()

alp = {}
answer = ()
for i in word:
    if i not in alp:
        alp[i] = 1
    elif i in alp:
        alp[i] += 1
print(alp)
for j in alp[key]:
    print(j)
