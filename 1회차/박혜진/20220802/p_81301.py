# 런타임 에러 코드
def change_num(word) :

  numbers = word
  num = {
  'zero' : 0,
  'one' : 1,
  'two' : 2,
  'three' : 3,
  'four' : 4,
  'five' : 5,
  'six' : 6,
  'seven' : 7,
  'eight' : 8,
  'nine' : 9
  }
  
  for n in num :
    if n in numbers :
      numbers = numbers.replace(n, str(num[n]))

  return int(numbers)

print(change_num(input()))



# 정답 코드
def solution(s):
    answer = s 
    num_s = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    
    for item in num_s.items():
        answer = answer.replace(item[0], str(item[1]))   


    return int(answer)