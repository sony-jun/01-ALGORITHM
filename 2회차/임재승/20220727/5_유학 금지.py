# https://www.acmicpc.net/problem/2789

li = (input())
answer = ''
remove_set = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']


li = [i for i in li if i not in remove_set]

for idx in li:
    answer += idx

print(answer)

