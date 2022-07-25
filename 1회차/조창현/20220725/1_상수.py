# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")
# 734 893

a, b = input().split()
re_a = []
re_b = []
re_anum = ''
re_bnum = ''
# 입력받은 문자열을 re_a 리스트에 하나씩 넣어준다.
for i in a:
    re_a.append(i)
# 슬라이싱을 통해 re_a 뒤집어 준다.
re_a = re_a[::-1]
#print(re_a)

for i in b:
    re_b.append(i)
re_b = re_b[::-1]
#print(re_b)
# 뒤집은 re_a를 re_anum 문자열에 하나씩 붙여준다.
for i in re_a:
    re_anum += str(i)
#print(re_anum)

for i in re_b:
    re_bnum += str(i)
#print(re_bnum)

if int(re_anum) < int(re_bnum):
    print(re_bnum)
else:
    print(re_anum)