import sys


sys.stdin = open("2_크로아티아 알파벳.txt")


change = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
n = input()

for i in change :
    n = n.replace(i, '*')  # 알파벳을 기호로 교체(한글자로 바꿔 카운트 대체)

print(len(n)) # 바뀐 알파벳의 갯수 = 문자열의 길이