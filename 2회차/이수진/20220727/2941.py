a=input()
alpha=['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in alpha: # 크로아티아 알파벳 리스트에서 돕니당
    a=a.replace(i, '*') # 단어 속 크로아티아 알파벳을 한글자(*)로 바꿉니다

print(len(a))#변환된 단어의 갯수를 출력합니다