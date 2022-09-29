N = input()
word = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']    
word_count = 0
for a in word:                                              # 해당 단어를 순회하며 입력값에서 찾는다.
    word_count += N.count(a)                                # 단어를 찾은 만큼 카운트 해주고
    N = N.replace(a, ' ')                                   # 찾은 단어를 제거하고 공백으로 채운다. 이 때 공백으로 채우지 않으면, 
                                                            # 단어가 빠지고 나서 새로운 단어가 만들어지고 카운트 될 수 있기 때문이다.
print(word_count + len(N) - N.count(' '))                   # 카운트된 단어 개수와 남은 문자들의 길이, 
                                                            # 그리고 그 길이에 포함되어 있는 공백의 수를 제거하여 출력한다.