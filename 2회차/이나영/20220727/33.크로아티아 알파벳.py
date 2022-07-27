from re import A
import sys

sys.stdin = open("33.크로아티아 알파벳.txt")

# 1) 문제 이해 : 20min소요
# output값은 몇개의 크로아티아 알파벳이냐. output은 몇개의 크로아 알파벳이냐. 
# # 크아알파 아닌 알파벳은 한 글자씩 센다.
# 2) 문제 접근 : 25min소요
# 크로아 를 list로. for문으로 순회. count써서 갯수 출력. 일단 드가보자.

word = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']


for alphabet in croatia :
# =======================여기까지 내 힘으로 했고, for문으로 count쓰려면 맞으면 세고 아니어도 세.
# 라고 할랬더니 for문에 while문에 난리났는데, 오늘 배운 replace로도 가능하대니까 해봐. (40min소요)
    word = word.replace(alphabet, '-') # -로 바꿔주라는건데, 그리고 그 len(길이)를 세라는건데..그럼 아닌 알파벳은?
print(len(word))

