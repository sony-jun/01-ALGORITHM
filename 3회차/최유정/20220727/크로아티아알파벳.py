# https://www.acmicpc.net/problem/2941

input_ = input().split() # ljes=njak
list_ = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
counter = 0

for i in input_:
    if i in list_:
        counter += 1
print(counter)

