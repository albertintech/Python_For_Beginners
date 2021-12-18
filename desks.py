a = int(20)
b = int(21)
c = int(22)

def calc(students):
    rem = students % 2
    desks = students // 2
    return desks + rem
  
print(calc(a) + calc(b) + calc(c))
