#백준 가장 많은 글자 1371
# 영어에서는 어떤 글자가 다른 글자보다 많이 쓰인다. 예를 들어, 긴 글에서 약 12.31% 글자는 e이다.
# 어떤 글이 주어졌을 때, 가장 많이 나온 글자를 출력하는 프로그램을 작성하시오.
import sys
sys.stdin = open("04_성장_ 가장많은글자.txt")
s = sys.stdin.read()
text = s.replace('\n', '').replace(' ', '')
my_dic = {}
for i in text:
    if i not in my_dic:
        my_dic.update({i: 1})
    elif i in my_dic:
        my_dic[i] += 1
N = [k for k, v in my_dic.items() if max(my_dic.values()) == v]
answer = sorted(N)
print(*answer,sep='')





