import sys
sys.stdin = open("49_회사에 있는 사람_7785.txt", "r")

# enter: True, leave: False
# 딕셔너리 추가

T = int(input())

dic = {}
for tc in range(T):
    name, TF = input().split()
    if TF == "enter":
        dic[name] = TF
    else:
        del dic[name]

dic = sorted(dic.keys(), reverse=True)

for i in dic:
    print(i)