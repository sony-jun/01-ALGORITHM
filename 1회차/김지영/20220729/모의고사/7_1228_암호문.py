# n = 0 ~ 999999(1000000)
# | x y s
# 앞에서부터 x의 위치[x-1] 다음에
# if x = 1, insert(1=x,s)
# y개의 
# 숫자열 s 삽입, y = len(s) 
import sys
sys.stdin = open("input.txt", "r")
T = 10
for test_case in range(1,T+1):
    
    OriPW_length = int(input())     # 첫번째 줄 : 원본 암호문의 길이 OriPW_length
    OriPw = input().split()         # 두번째 줄 원본 암호문 OriPW
    Ctrl_Num = int(input())         # 세번째 줄 : 명령어의 개수 Ctrl_Num
    Ctrl = input().split('I')       # 네번째줄 명령어   Ctrl
    # # Ctrl 다듬기
    Ctrl.remove('')
    for i in range(Ctrl_Num):
        Ctrl[i] = Ctrl[i].split(' ')
        Ctrl[i].remove('')
        Ctrl[i].pop()
    # Ctrl[i][0] = x
    # Ctrl[i][1] = y
    # Ctrl[i][2:] = s
    def PW(x,s):
        for i in s[::-1]:
            OriPw.insert(int(x),i)

    # lst = [0,1,2,3]
    # lst_test = ['a','b','c']
    # k = 1
    # for i in lst_test[::-1]:
    #     lst.insert(1,i)
    # print(lst)
    for ctrl in Ctrl:
        x = ctrl[0]
        s = ctrl[2:]
        # print(s,type(s))
        PW(x,s)
    result = ' '.join(OriPw[:10])

    # print(OriPW_length)
    # print(OriPw)
    # print(Ctrl_Num)
    # print(Ctrl)
    print(f'#{test_case}',result)
