# s, k, h
s, k, h = map(int, input().split())

sum_ = s + k + h
if sum_ >= 100:
    print('OK')
else:
    if s < k and s < h:
        print('Soongsil')
    if k < s and k < h:
        print('Korea')
    if h < s and h < k:
        print('Hanyang') 