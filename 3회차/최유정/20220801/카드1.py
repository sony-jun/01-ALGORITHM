# https://www.acmicpc.net/problem/2161

N = int(input()) #7
queue = list(range(1, N+1)) #1,2,3,4,5,6,7

while len(queue) > 1:
    print(queue.pop(0), end = ' ')
    queue.append(queue.pop(0))
print(queue[0])
