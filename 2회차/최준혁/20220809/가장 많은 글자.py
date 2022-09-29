import sys
dict = {}
a = []
max = 0
S = list(map(str, sys.stdin.read().replace(" ", "").replace("\n", "")))
for char in S:
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1

for k, v in dict.items():
    if max < v:
        max = v

for k, v in dict.items():
    if max == v:
        a.append(k)

a.sort()
for i in a:
    print(i, end='')

# import sys
# eng = 'abcdefghijklmnopqrstuvwxyz'
# result = []
# inp = sys.stdin.read()

# for i in eng:
#     result.append(inp.count(i))

# m = max(result)
# for i in range(len(result)):
#     if m == result[i]:
#         print(chr(i+97), end = '')