import sys

sys.stdin = open('1371.txt')
letter = sys.stdin.read()
#print(letter)
letter = letter.replace('\n',"")
letter = letter.replace(" ",'')

#print(letter)

alph = [0 for i in range(26)]

for x in letter:
    if x.islower(): 
        alph[ord(x)-97] += 1 #아스키코드로 변환
           
for i in range(26):
    if alph[i] == max(alph): #제일 많은 알파벳이 있다면
        print(chr(i+97), end='') #다시 숫자로 출력해라

