my_dic = {'Soongsil': 0, 'Korea': 0, 'Hanyang': 0}
S, K, H = map(int, input().split())

my_dic['Soongsil'] += S
my_dic['Korea'] += K
my_dic['Hanyang'] += H
if S + K + H < 100:
    print(*[k for k,v in my_dic.items() if min(my_dic.values())==v])
else:
    print('OK')