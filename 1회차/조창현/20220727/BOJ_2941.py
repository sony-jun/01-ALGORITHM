word = input()
## 순순한 알파벳의 수
word_len = len(word)
## 두 글자로 이루어진 크로아알파
croa2_alpha = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
## 세 글자로 이루어진 크로아알파
croa3_alpha = ['dz=']
m2 = []
m3 = []
## 두 글자로 이루어진 크로아알파를 찾아 몇개가 있는지 리스트로 정리한다.
for i in croa2_alpha:
    m2.append(word.count(i))
#print(m2)
## 세 글자로 이루어진 크로아알파를 찾아 몇개가 있는지 리스트로 정리한다.
for i in croa3_alpha:
    m3.append(word.count(i))
#print(m3)
## 전체 알파벳의 수에서 두글자로 이루어진 세글자로 이루어진 수를 빼준다.
## 여기서 세글자로 이루어진 수를 -2 해줘야 한다고 생각했지만 
## 두글자로 이루어진 'z=' 과 세글자로 이루어진 'dz='가 뒷부분이 겹쳐서 그냥 빼줘도 답이 나온다.
croa_len = word_len - sum(m2) - sum(m3)

print(croa_len)