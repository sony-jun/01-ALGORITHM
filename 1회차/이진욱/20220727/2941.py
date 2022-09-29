N=input()
S=['c=','c-','dz=','d-','lj','nj','s=','z='] # 변환해야되는 리스트

for i in range(len(S)):
    if S[i] in N:

        N=N.replace(S[i],'5') # 알파벳 소문자와 '-', '='로만 이루어져 있다. 

print(len(N))

# input
# ljes=njak -> 5 e 5 5 a k -> 6
# ddz=z=
# nljj