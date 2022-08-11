def solution(s):
    answer = 0
    idx=0
    while idx<len(s):
        if(s[idx]=='o'):
            idx=idx+3
            answer=answer*10+1
        elif(s[idx]=='t'):
            if(s[idx+1]=='w'):
                idx=idx+3
                answer=answer*10+2
            else:
                idx=idx+5
                answer=answer*10+3
        elif(s[idx]=='f'):
            if(s[idx+1]=='o'):
                idx=idx+4
                answer=answer*10+4
            else:
                idx=idx+4
                answer=answer*10+5
        elif(s[idx]=='s'):
            if(s[idx+1]=='i'):
                idx=idx+3
                answer=answer*10+6
            else:
                idx=idx+5
                answer=answer*10+7
        elif(s[idx]=='e'):
            idx=idx+5
            answer=answer*10+8
        elif(s[idx]=='n'):
            idx=idx+4
            answer=answer*10+9
        elif(s[idx]=='z'):
            idx=idx+4
            answer=answer*10
        else:
            answer=answer*10+int(s[idx])
            idx+=1
    return answer