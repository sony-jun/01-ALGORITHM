# 다이얼

word = input()
dial_number = {                     
    'ABC' : 2,
    'DEF' : 3,
    'GHI' : 4,
    'JKL' : 5,
    'MNO' : 6,
    'PQRS' : 7,
    'TUV' : 8,
    'WXYZ': 9
}
result = 0
for i in word:                          # 입력값의 문자열 순회
    for j in dial_number:               # 딕셔너리 key를 순회하며 비교
        if i in j:                      # key 내부에 존재하면
            result += dial_number[j]    # key에 해당하는 value값을 result에 더함
print(result + len(word))               # 걸리는 시간은 해당하는 다이얼을 모두 더한 값에
                                        # 입력값의 길이를 더한 값과 같다.