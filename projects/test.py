operSign = ['+', '-', '*', '/']

msg_1 = "Enter an equation"
msg_2 = "Do you even know what numbers are? Stay focused!"
msg_3 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_4 = "Yeah... division by zero. Smart move..."

while True:
    print(msg_1)
    equation = input().split(" ")
    try:
        x = float(equation[0])
        oper = equation[1]
        y = float(equation[2])
    except:
        print(msg_2)
        continue

    if oper not in operSign:
        print(msg_3)
        continue

    if oper == '+':
        print(x + y)
        break
    elif oper == '-':
        print(x - y)
        break
    elif oper == '*':
        print(x * y)
        break
    elif oper == '/' and y != 0:
        print(x / y)
        break
    else:
        print(msg_4)
