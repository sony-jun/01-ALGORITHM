croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
val = input()
temp = len(val)
answer = 0

for i in croatia:
    # 만약 크로아티아 알파벳이 있으면
    if val.count(i) > 0:
        # 발견된 개수만큼 카운트하고
        # 초기 입력값 길이에 발견된 개수만큼 빼주고
        # 원래 입력값에서 지운다.
        answer += val.count(i)
        temp -= len(i) * val.count(i)
        # "nljj" 와 같은 케이스 때문에 "lj" 를 지우고 나서 해당 자리에 공백을 넣어준다.
        val = val.replace(i, " ", val.count(i))
  
# 나머지 글자들 수만큼 더 함.
answer += temp

print(answer)