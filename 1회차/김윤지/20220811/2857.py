

noFBI = True #아닌게 참
for i in range(1,6): # i를 바로 출력하기 위해 1~6까지 범위설정
    name = input()
    # print(name)

    if 'FBI' in name: #name에 FBI가 들어가면 
        print(i)   #숫자출력
        noFBI = False # 거짓이라서 멈춤
if noFBI:# 참이면 'HE GOT AWAY!' 출력
    print("HE GOT AWAY!")