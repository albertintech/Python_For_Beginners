msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
# digits = '1234567890'


def is_one_digit(v):
    if (v > -10 and v < 10) and (v - int(v) == 0):
        return True
    else:
        return False


def check(v1, v2, v3):
    msg = ''
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg += msg_7
    if (v1 == 0 or v2 == 0) and (v3 in ['*', '+', '-']):
        msg += msg_8
    if msg != '':
        msg = msg_9 + msg
        print(msg)


memory = 0
while True:
    print(msg_0)
    calc = input()
    x, oper, y = calc.split()

    if x == "M":
        x = memory
    if y == "M":
        y = memory

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
        continue
    else:
        if oper in ["+", "-", "*", "/"]:
            check(x, y, oper)
            if oper == '+':
                result = x + y
            elif oper == '-':
                result = x - y
            elif oper == '*':
                result = x * y
            elif oper == '/' and y != 0:
                result = x / y
            else:
                print(msg_3)
                continue
            print(result)

            while True:
                print(msg_4)
                ans = input()
                if ans == 'y':
                    memory = result
                    break
                elif ans == 'n':
                    break

            while True:
                print(msg_5)
                ans = input()
                if ans in ['n', 'y']:
                    break

            if ans == 'n':
                break
            else:
                continue
        else:
            print(msg_2)
            continue
