# https://www.acmicpc.net/problem/2941
# 크로아티아 알파벳

# 풀이
croatia_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia_alphabet:
    word = word.replace(i, 'j')

print(len(word))