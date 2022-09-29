#reverse나 [::-1] 사용 가능?
x, y = map(str, input().split())
total = str(int(x[::-1]) +int(y[::-1]))
print(int(total[::-1]))
#int와 str에 대해 더 공부해야겠다,,,