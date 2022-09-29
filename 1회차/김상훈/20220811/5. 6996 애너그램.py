import sys
sys.stdin = open("5. 애너그램.txt", "r")

T = int(input())
for _ in range(T):
    word = input().split() # 두 문장 입력받음
    word1 = word[0]  # 앞 단어과 뒷 단어으로 나눠서 각각 저장
    word2 = word[1]

    word1_list = [] # 앞단어와 뒷 단어 넣을 리스트
    word2_list = []

    for i in word1:
        word1_list.append(i)
    for j in word2:
        word2_list.append(j) # 각각 리스트에 넣어준다.

    word1_list.sort()    # 각각 정렬
    word2_list.sort()
    if word1_list == word2_list: # 정렬 한 리스트가 같으면.
        print(f'{word1} & {word2} are anagrams.') 
    else: # 다르면 
        print(f'{word1} & {word2} are NOT anagrams.')
    