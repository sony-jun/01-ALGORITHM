# emoji = [':-)', ':-(']
h = ':-)'
s = ':-('
h_cnt = 0
s_cnt = 0

stns = input().replace(' ', '')
h_cnt = stns.count(h)
s_cnt = stns.count(s)

if h_cnt > s_cnt:
    print('happy')
elif s_cnt > h_cnt:
    print('sad')
elif h_cnt == s_cnt and h_cnt > 0 and s_cnt > 0:
    print('unsure')
elif h_cnt == 0 and s_cnt == 0:
    print('none')
