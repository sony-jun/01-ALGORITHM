from re import A
import sys

sys.stdin = open("32.단어공부.txt")

word = input().lower() # 입력받은 문자열을 소문자로 변환해주기. #word = mississipi
word_list = list(set(word)) #set을 사용해서 중복을 제거한 후 리스트()로 묶기. #word_list = ["m","i","s","p"]
cnt = [] # 가장많이 사용된 알파벳을 알기 위해 cnt변수를 []리스트로 초기화.

for i in word_list: # type : word_list(list), word(str), cnt(list) / word_list안에 문자 for문으로 반복
    count_ = word.count(i) # count 변수를 새로 만들어서 중복되는 문자를 제외하기 전 입력받은 word변수에서 문자가 몇개였는지 세고
    cnt.append(count_) # cnt변수 리스트에 count를 append, 추가해준다.#그러면 M=1, i=4, s=4, p=1이 됨
   
if cnt.count(max(cnt)) >= 2: #if문을 사용해서 cnt변수 리스트에 max를 count()함수를 이용해서 센 수가
    print("?") #cnt변수 리스트에 2개 이상이라면 가장많이 사용된 게 많으니까 "?" 출력

else:
    print(word_list[(cnt.index(max(cnt)))].upper()) # upper는 대문자출력.
    

# 그 나머지를 예를 들면 word = baaaa의 경우 word_list = [b,a], cnt = [1,3] // max(cnt)는 3이되고
# index(3)은 cnt에서 cnt[1]에 위치하기 때문에 즉, index자체가 가리키는 3이 cnt[1]이기 때문에 word_list[1]은
# a를 가리키는데 그것이 uppercase()로 인해 대문자로만 출력되기 떄문에 A가 출력된다.