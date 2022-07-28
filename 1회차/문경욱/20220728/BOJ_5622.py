# 딕셔너리로 풀이
dial_dict = {'ABC' : 3, 'DEF': 4,'GHI':5, 'JKL':6, 'MNO':7, 'PQRS': 8, 'TUV':9, 'WXYZ':10}

words = input()
time_ = 0

# 입력 받은 문자를 한 글자씩 뽑고
for letter_ in words:
    # dial_dict의 키 값도 하나씩 뽑아서
    for dial_letter in dial_dict.keys():
        # 만약 글자가 dial_dict의 키값 안에 있다면
        if letter_ in dial_letter:
            # 키값에 해당하는 value값을 time_ 변수에 더한다.
            time_ += dial_dict.get(dial_letter)

print(time_)


'''
리스트로 문제 풀이
# 알파벳 묶음을 만듦
dial_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# 걸리는 시간 : 3      4      5      6      7      8       9      10

# 사용자로부터 입력
words = input()

# 총 걸리는 시간 선언
time_ = 0

# dial_list에 있는 알파벳들을
for alphabet in dial_list:
    # 한 글자씩 분리하고
    for j in alphabet:
        # words 단어를 한 글자씩 분리해서
        for k in words:
            # 만약 두 글자가 같으면
            if j == k:
                # dial_list의 인덱스 값 + 3을 time_변수에 더한다.
                time_ += dial_list.index(alphabet) + 3

print(time_)
'''