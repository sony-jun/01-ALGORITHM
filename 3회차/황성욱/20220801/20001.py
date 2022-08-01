debug = input()
cnt = 0
while debug != '고무오리 디버깅 끝':
    debug = input()
    if debug == '문제':
        cnt += 1
    
    elif cnt <= 0 and debug == '고무오리':
        cnt += 2
    
    elif debug == '고무오리':
        cnt -= 1
    
if cnt == 0:
    print('고무오리야 사랑해')
else:
    print('힝구')

