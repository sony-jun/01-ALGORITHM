# https://www.acmicpc.net/problem/1157
# 단어 공부

# 풀이
word = input().upper()
alphabet = {}
cnt_max = []

for i in range(len(word)):
    if word[i] not in alphabet:
        alphabet[word[i]] = 1
    elif word[i] in alphabet:
        alphabet[word[i]] += 1

for j in alphabet:
    if alphabet[j] == alphabet[max(alphabet, key = alphabet.get)]:
        cnt_max.append(j)

if len(cnt_max) > 1:
    print('?')
else:
    print(max(alphabet, key = alphabet.get))