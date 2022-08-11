fbi = [] #fbi 이름 리스트
cnt = 0 #fbi가 몇 명인지

for i in range(5):
    name = input()
    fbi.append(name)  #fbi에 이름 추가

for j in range(len(fbi)):
    if 'FBI' in fbi[j]:  #j = [0, 2, 4]
        print(j+1, end = ' ') #1 3 5
        cnt = 1

if cnt == 0:
    print('HE GOT AWAY!')


# FBI = []

# for i in range(1, 6):
#     name = input()
#     if 'FBI' in name:
#         FBI.append(i)
# if FBI:
#     print(*FBI)

# else:
#     print('HE GOT AWAY!')