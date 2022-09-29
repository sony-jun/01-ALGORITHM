croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# 크로아티아 문자들이 포함된 리스트를 정의해준다.
word = input()

count = 0
for i in range(len(word) - 1):
    if word[i] + word[i + 1] in croatia:
        count += 1
# 2개의 낱말로 된 문자중에 크로아티아 문자가 있으면 카운트 값을 1 추가해준다.
for i in range(len(word) - 2):
    if word[i] + word[i + 1] + word[i + 2] in croatia:
        count += 1
# 3개의 낱말로 된 크로아티아 문자는 2개의 낱말로 된 크로아티아 문자에 다른 값 하나가
# 추가된 형태이기에 1만 더 카운트 해준다.        
print(len(word) - count)
# 입력값에서 크로아티아 문자를 표현하기 위해 사용된 문자를 카운트 한 값만큼 빼준다.
