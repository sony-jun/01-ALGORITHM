s = input()
s = s.split('(^0^)')
l,r = s[0].count('@'),s[1].count('@')
print(l,r,sep=' ')