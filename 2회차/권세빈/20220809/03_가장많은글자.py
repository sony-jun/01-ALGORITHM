import sys
sys.stdin = open('03.txt','r')

# sys.stdin.read()를 통해서 EOF가 발생할 때 까지 입력을 받을 수 있다.

# 소문자 알파벳 카운트를 셀 때, 리스트 범위에 벗어나지 않도록
# 공백과 개행을 없애준다.
n = sys.stdin.read().replace(' ','').replace('\n','')

# 모든 알파벳의 개수 체크용 리스트
a = [0] * 26

for i in n:
    a[ord(i)-97] += 1

for j in range(26):
    if a[j] == max(a):
        print(chr(j+97), end='')