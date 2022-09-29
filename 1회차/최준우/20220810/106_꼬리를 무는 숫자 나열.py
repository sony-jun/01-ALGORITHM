# https://www.acmicpc.net/problem/1598

a, b = map(int, input().split())
def cal(temp):
    x = (temp - 1) // 4 
    y = (temp - 1) % 4
    return [x, y]
co_a = cal(a)
co_b = cal(b)

result = 0
if co_a[0] > co_b[0] :
    result += co_a[0] - co_b[0]
else:
    result += co_b[0] - co_a[0]
if co_a[1] > co_b[1] :
    result += co_a[1] - co_b[1]
else:
    result += co_b[1] - co_a[1]
print(result)