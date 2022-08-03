change = {'b':'d', 'd':'b', 'p':'q', 'q':'p'}

T = int(input())

for i in range(1, T+1):
    mirror = ''
    string = input()
    string = reversed(string)

    for j in string:
        mirror += change[j]
    print(f'#{i} {mirror}')