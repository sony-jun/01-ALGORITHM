# 단순단순
def solution(s):
  answer = s 
  answer = answer.replace('zero', '0')
  answer = answer.replace('one', '1')
  answer = answer.replace('two', '2')
  answer = answer.replace('three', '3')
  answer = answer.replace('four', '4')
  answer = answer.replace('five', '5')
  answer = answer.replace('six', '6')
  answer = answer.replace('seven', '7')
  answer = answer.replace('eight', '8')
  answer = answer.replace('nine', '9')
  return int(answer)

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))

# 딕셔너리버전