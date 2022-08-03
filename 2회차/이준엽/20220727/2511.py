a_card = list(map(int,input().split()))
b_card = list(map(int,input().split()))

a_sum = 0
b_sum = 0
winner = ''

for i in range(len(a_card)):
    if a_card[i] > b_card[i]:
        a_sum+=3
    elif a_card[i] < b_card[i]:
        b_sum+=3
    else:
        a_sum+=1
        b_sum+=1

if a_card == b_card:
    winner = 'D'
elif a_sum > b_sum:
    winner = 'A'
elif a_sum< b_sum:
    winner = 'B'
elif a_sum == b_sum:
    for i in range(len(a_card)):
        if a_card[len(a_card)-1-i] > b_card[len(a_card)-1-i]:
            winner = 'A'
            break
        elif a_card[len(a_card)-1-i] < b_card[len(a_card)-1-i]:
            winner = 'B'
            break

print(f'{a_sum} {b_sum}',winner,sep='\n')




















# a_card = list(map(int,input().split()))
# b_card = list(map(int,input().split()))

# a=0
# b=0

# for i in range(len(a_card)):
#     if a_card[i]>b_card[i]:
#         a+=3
#     elif a_card[i]<b_card[i]:
#         b+=3
#     else:
#         a+=1
#         b+=1
# print(a,b)
# if a>b:
#     print('A')
# elif a<b:
#     print('B')
# elif a==b:
#     if a_card[len(a_card)-1]>b_card[len(a_card)-1]:
#         print('A')
#     elif a_card[len(a_card)-1]<b_card[len(a_card)-1]:
#         print('B')
#     else:
#         print('D')