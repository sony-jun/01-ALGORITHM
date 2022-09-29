s, k, h = map(int,input().split()) #숭실:s, 고려:k, 한양:s

if s + k + h < 100 : #합이 100이 아니면
    if s < k and s < h : #s가 k,h 보다 작으면
        print('Soongsil') #숭실
    elif k < h and k < s : # k가 s,h보다 작으면
        print('Korea') #고려
    else : #둘 다 아니라면
        print('Hanyang') #한양
else : #합이 100이상이면
    print('OK')