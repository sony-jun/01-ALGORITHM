import sys
def croatia(str0):
    answer=len(str0)
    temp0=""
    temp1=""
    for i in str0:
        if(i=='='):
            if(temp0=="c" or temp0=="s"):
                answer-=1
            elif(temp0=='z'):
                if(temp1=='d'):
                    answer-=2
                else:
                    answer-=1    
        elif(i=='-'):
            answer-=1
        elif(i=="j"):
            if(temp0=="l" or temp0=="n"):
                answer-=1
        temp1=temp0
        temp0=i
    return answer
sys.stdin=input()
print(croatia(sys.stdin))
