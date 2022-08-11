s,k,h = map(int,input().split()) # 세 학교의 참여도
skh_list = []
skh_list.append((s,'Soongsil'))
skh_list.append((k,'Korea'))
skh_list.append((h,'Hanyang'))
total = 0
for i in skh_list:
    total += i[0]
print('OK' if  total >= 100 else min(skh_list)[1])