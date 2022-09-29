import sys
word = sys.stdin.read() 
alphabet = list(range(97, 123)) # 아스키 코드를 통해서 리스트 생성
a = {}
for x in alphabet: # for문 통해서 x 처음부터 끝까지 순회
    a[chr(x)]=word.count(chr(x))
for x in a:
    if a[str(x)] == max(a.values()): # 최대숫자와 같으면
        print(x, end='')