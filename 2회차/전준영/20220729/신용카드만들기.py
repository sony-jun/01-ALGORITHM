T = int(input())
answer=[]
for test_case in range(1, T + 1):
    Tk=input()
    an=len(Tk)
    for k in Tk:
        if(k=='-'):
            an-=1
    if(an==16 and (int(Tk[0])>2 and int(Tk[0])<7 or int(Tk[0])==9)):
        answer.append('1')
    else:
        answer.append('0')
for j in range(0,T):
    print("#"+str(j+1),answer[j])