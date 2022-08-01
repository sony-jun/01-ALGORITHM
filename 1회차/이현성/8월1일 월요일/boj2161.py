a = int(input())
list_ = [i for i in range(1, a + 1)]
fall = []

while True:
    fall.append(list_.popleft())
    if not list_:
        break
    list_.append(list_.popleft())

print(fall)