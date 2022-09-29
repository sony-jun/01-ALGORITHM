from re import A
import sys

sys.stdin = open("32_단어공부.txt")

# N = input()
# list(N)
# n = N.lower()
# list(n)

# a = n.count('m')
# b = n.count('i')
# c = n.count('s')
# d = n.count('p')

# if a != b != c != d:
#     print(max(a, b, c, d))
# else:
#     print('?')

N = str(input())
N = N.upper()
N_list = list(set(N))
cnt = []
for a in range(len(N_list)): #여기까지는 생각이 들었다.
    cnt.append(list(N).count(N_list[a])) # a는 변수이며 아무알파벳이 들어가도된다.
Max = max(cnt) # 갯수 중에서 가장 큰값을 꺼내는 것이다.
if cnt.count(Max) != 1: # 꺼낸 갯수가 1과 같지 않으면 ?가 나오고
    print('?')
else:
    print(N_list[cnt.index(Max)])
