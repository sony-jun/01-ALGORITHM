def rev(word):
    s_word = str(word)
    word2 = s_word[::-1]

    word3 = int(word2)
    return word3

# rev()를 입력된 숫자를 문자열로 바꾸어 거꾸로 출력하고 다시 정수로 바꾸어 변환하게 하였습니다.
# 이 경우 가장 앞 자리가 0이면 그 자릿수 값이 0이라고 인식 다음 자릿수 확인을 하기 때문에 
# 원하는 값을 받는데 이상이 없었습니다.

x, y = map(int, input().split())
result = rev(rev(x) + rev(y))
print(result)

# 그리고 입력될 두 값을 문제에서 원하는 방식대로 계산하여주고 값을 출력해주었습니다.