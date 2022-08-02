t = int(input())
oxList =[]
for i in range(t):
    vps = input()
    while True:
        try:
            vps = vps.replace('()','') #모든 ()를 없애기
            vps.index('()') #()의 위치를 계속 찾기
        except ValueError:
            break # ()가 없으면 break

    if len(vps) == 0:
        oxList.append('yes') #모든 ()를 없애서 문자열이 남지 않는다면 vps
    else:
        oxList.append('no') #문자열이 남았다면 vps가 아님

for i in oxList:
    print(i)