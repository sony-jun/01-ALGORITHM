alpa = {
    'ABC' : 3,
    'DEF' : 4,
    'GHI' : 5,
    'JKL' : 6,
    'MNO' : 7,
    'PQRS' : 8,
    'TUV' : 9,
    'WXYZ' : 10
}

dial = input()

sum = 0

for d in dial :
  for a in alpa :
    if d in a :
      sum += alpa[a]

print(sum)