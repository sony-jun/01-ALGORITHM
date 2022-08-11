import sys
sys.stdin = open('116_input.txt')
FBI_list = []
for i in range(1,6):
    name = input()
    if 'FBI' in name:
        FBI_list.append(str(i))
# print(FBI_list)
if FBI_list != [] :
    ops = ' '.join(FBI_list)
    print(ops)
else : print('HE GOT AWAY!')