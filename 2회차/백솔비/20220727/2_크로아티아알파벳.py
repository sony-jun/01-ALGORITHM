import sys
sys.stdin = open("2_크로아티아알파벳.txt")

croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = input()

for alphabet in croatia:
    word = word.replace(alphabet, '#')

print(len(word))
