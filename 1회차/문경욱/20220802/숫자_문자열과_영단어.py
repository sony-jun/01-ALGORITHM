def solution(s):
    # 알파벳에 대응되는 숫자를 가진 딕셔너리 생성
    num_dict = {'zero' : 0 , 'one' : 1 , 'two' : 2 , 'three' : 3 ,'four' : 4, 'five' : 5 , 'six' : 6 , 'seven' : 7 , 'eight' : 8 , 'nine' : 9 }
    answer = ''
    num_list = []
    word_list = ''

    # 입력받은 s에 대해
    for char in s:
        # 만약 그 글자가 숫자라면
        if char.isdigit() == True :
            # num_list에 더하기
            num_list.append(int(char))
        # 만약 그 글자가 숫자가 아니라면
        else:
            # word_list에 더하기
            word_list += char
            # word_list의 글자가 딕셔너리 키에 해당한다면
            if word_list in num_dict :
                # num_list에 딕셔너리의 밸류를 더하고
                num_list.append(num_dict[word_list])
                # word_list는 초기화
                word_list = ''
            else:
                continue
    for num in num_list:
        answer += str(num)


    return int(answer)

print(solution('one4seveneight'))