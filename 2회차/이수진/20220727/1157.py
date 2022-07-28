a=input() 
a=a.upper()# 대문자로 변환
result={}
answer=[]
for i in range(65,91): #26번 검사
    if chr(i) in a :
        result[chr(i)]=int(a.count(chr(i)))
result = sorted(result.items(),key=lambda x:x[1],reverse=True)
#              (리스트형식으로 반환, 인덱스[1]번=value, 내림차순정렬)
for i in result: #가장 많은 알파벳과 같은 갯수의 알파벳 저장
    if result[0][1] == i[1]:
        answer.append(i[0])
if len(answer)==1: # 찾아낸 알파벳 갯수가 1보다 많으면 ?출럭
    print(*answer)
else :
    print('?')



text_ = input()
a = text_.upper()
result = list(a)
cnt = {}
for j in result:
    if j in cnt:
        cnt[j] += 1
    else:
        cnt[j] = 1
print('?') if len([k for k,v in cnt.items() if max(cnt.values()) == v]) > 1 else print(max(cnt, key=cnt.get))