import sys

sys.stdin = open("45_다이얼.txt")

alphabet = {'ABC':3,'DEF':4,'GHI':5,'JKL':6,'MNO':7,'PQRS':8,'TUV':9,'WXYZ':10}
word=input()
time=0
for i in range(len(word)):
    for j in alphabet.keys():
        if word[i] in j:
            time+=alphabet[j]
print(time)