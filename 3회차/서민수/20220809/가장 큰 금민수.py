
"""
N보다 작고 4 또는 7로 이루어진 수 중 가장 큰 수를 찾아라
"""

# 숫자 N입력
N = int(input())


# 초기 가장 큰 값 N은 4이상
max_ = 4

for number in range(N):
    # 숫자를 문자열로 변환
    string_number = str(number)

    # 각 숫자의 자릿수 값 확인
    for char_number in string_number:
        # 각 자릿수가 4 또는 7로만 이루어져있는지 확인
        # 각 자릿수가 4 또는 7로만 이루어져있지 않으면 반복을 멈추면된다
        if not (char_number != 4 or char_number != 7):
            break

    # for ~ else
    # for가 정상적으로 다 완료되면 else가 실행된다
    # break를 만나지 않으면 else가 실행된다
    else:
        print(string_number)