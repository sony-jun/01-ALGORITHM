# 666 들어간 영화만 만드는데

N = int(input()) #몇번쨰 영화인가
cnt = 0
a =0
while True:
    a += 1
    str_a = list(str(a))
    for b in range(len(str_a)-2):
        if str_a[b] == '6':
            if str_a[b+1] == '6':
                if str_a[b+2] == '6':
                    cnt += 1
                    break
    if cnt == N:
        break

print(a)
