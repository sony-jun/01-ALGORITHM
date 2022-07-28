# import sys
# sys.stdin = open("2_다이얼.txt", 'r')

push = input()

dial_alpha ={
    7 : [],
    8 : [],
    9 : []
    }
i = 25

while i >= 15:
    if i <= 18:
        dial_alpha[7].append(chr(i + 65))
    
    elif i <= 21:
        dial_alpha[8].append(chr(i + 65))

    elif i <= 25:
        dial_alpha[9].append(chr(i + 65))
    
    i -= 1

while i < 15:
    if (i % 3) - 2 == 0:
        dial_alpha[((i // 3) + 2)] = []
    dial_alpha[((i // 3) + 2)].append(chr(i + 65))
    i -= 1
    if i < 0:
        break
res = 0
for s in push:
    for k in dial_alpha:
        if s in dial_alpha[k]:
            res += k
res += len(push)
print(res)