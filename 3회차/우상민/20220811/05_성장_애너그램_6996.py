#백준 애너그램 6996
# 두 단어 A와 B가 주어졌을 때, A에 속하는 알파벳의 순서를 바꾸어서 B를 만들 수 있다면, A와 B를 애너그램이라고 한다.
# 두 단어가 애너그램인지 아닌지 구하는 프로그램을 작성하시오.
for i in range(int(input())):    # 3
    dic_1 = {}
    dic_2 = {}
    A, B = list(input().split())   #blather reblath
                                    # maryland landam
                                    # bizarre brazier
    for idx in A:
        if idx not in dic_1:
            dic_1[idx] = 1
        elif idx in dic_1:
            dic_1[idx] += 1
    for index in B:    
        if index not in dic_2:
            dic_2[index] = 1
        elif idx in dic_2:
            dic_2[index] += 1
    if dic_1 == dic_2:
        print(A,'&',B'are anagrams.')
    elif dic_1 != dic_2:
        print(A,'&',B'are NOT anagrams.')
