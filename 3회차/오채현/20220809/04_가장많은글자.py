# import sys

freq = {}
# stns = sys.stdin.read()
stns = input().replace(' ', '')

for char in stns:
    if char not in freq:
        freq[char] = 1
    else:
        freq[char] = freq[char] + 1

# print(freq)
maxV = 0
for v in freq.values():
    if v > maxV:
        maxV = v
print(maxV)


def getKey(v):
    keys = []
    for key, value in freq.items():
        if v == value:
            keys.append(key)
    keys.sort()
    return keys


print(*getKey(maxV))
