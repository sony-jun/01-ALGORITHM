import sys
sys.stdin = open("20220727/2941_크로아티아알파벳.txt")

word = input()
alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in alphabet:
    word = word.replace(i, '.')

print(len(word))