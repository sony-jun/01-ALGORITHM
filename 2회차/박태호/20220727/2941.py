#크로아티아 알파벳

croa = ['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt = 0
w = input() # ljes=njak
len_w = len(w) # 전체 길이에서 크로 뺄거임
#일단 croa 순회
for i in croa:
    cnt += w.count(i) # 해당문자 개수를 cnt에 저장  
         
print(len_w - cnt)