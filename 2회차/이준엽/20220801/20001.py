cnt = 0

while 1:
    i = input()
    if i == '문제':
        cnt+=1
    elif i == '고무오리' and cnt == 0:
        cnt+=2
    elif i == '고무오리':
        cnt-=1
    elif i == '고무오리 디버깅 끝':
        break
if cnt == 0 :
    print('고무오리야 사랑해')
else:
    print('힝구')