word = input().upper() # 대문자로 반환 word = MISSISSIPI. 대문자로 반환은 why? set에서 소문자와 대문자를 구분하기 때문에 대문자든 소문자든 바꿔주고 중복 제거. 
word_list = list(set(word))     # 문자열들의 중복제거하고 list
# word_list = [M, I, S, P] / [Z, A]
cnt = []        # cnt에 넣을 값 주머니(리스트)
for i in word_list:     
  count = word.count(i)        # count = word.count(i) -> word를 count해라.
  cnt.append(count)         # i에 해당하는 것을 count해라. count(M) -> word.count(M) -> 1개
                            # cnt [1, 4, 4, 1] / [2, 1]
if cnt.count(max(cnt)) > 1: # cnt.count(4) -> 2 -> 2 > 1 
  print("?")

else:       # cnt.count(2) -> 1 -> 1 > 1 -> false
  print(word_list[(cnt.index(max(cnt)))]) # cnt.index(2) -> 2가 첫번째에 있으니까 0 -> word_list[0] -> Z