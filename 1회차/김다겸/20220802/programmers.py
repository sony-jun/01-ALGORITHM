def solution(s):
    num_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    # s를 한글자씩 순회
    for i in range(len(s)):
        # num_list의 요소 순회
        for j in range(len(num_list)):
            # s의 3개의 문자가 num_list에 있는 요소이면
            if s[i:i+3] == num_list[j]:
                # s의 3개의 문자를 num_list에서 해당하는 문자의 인덱스로 변환
                s = s.replace(s[i:i+3], str(j))
            # s의 4개의 문자가 num_list에 있는 요소이면
            if s[i:i+4] == num_list[j]:
                # s의 4개의 문자를 num_list에서 해당하는 문자의 인덱스로 변환
                s = s.replace(s[i:i+4], str(j))
            # s의 5개의 문자가 num_list에 있는 요소이면
            if s[i:i+5] == num_list[j]:
                # s의 5개의 문자를 num_list에서 해당하는 문자의 인덱스로 변환
                s = s.replace(s[i:i+5], str(j))

    return int(s)

print(solution("one4seveneight"))