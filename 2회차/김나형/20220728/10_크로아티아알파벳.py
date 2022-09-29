import sys

sys.stdin = open("10_크로아티아알파벳.txt")

cro = ['c=','c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] # 크로아티아 문자 리스트로 저장
text = input() # 찾아야할 기준이 되는 문자
cnt = 0

# for i in range(len(cro)): # cro 리스트에 있는 모든 문자열을 text 값과 비교
#     if cro[i] in text: # 0부터 9까지 배열 안의 값이 text에 있다면
#         cnt += text.count(cro[i]) # 단어 갯수를 count
#         text = text.replace(cro[i],'') # 배열 값을 text에서 제거
# text = text.replace(' ','')
# print(cnt + len(text)) # count된 단어의 값과 남은 알파벳의 갯수를 더하여 출력

# cro = ['c=','c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# text = input()
# cnt = 0


for i in range(len(cro)):
    if cro[i] in text:
        text = text.replace(cro[i],' ')

print(len(text))