import sys
sys.stdin = open("3_문서검색.txt", 'r')

assembly_space = ''
doc = []
cnt = 0

doc.extend(sys.stdin.readline().rstrip())
word = sys.stdin.readline().rstrip()

while len(doc) != 0:
    assembly_space += doc.pop(0)
    if word in assembly_space:
        cnt += 1
        assembly_space = ''

print(cnt)