# My Solution

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = " You are"
operators = ['+', '-', '*', '/']
memory = 0


def is_one_digit(v):
    if (v > -10 and v < 10) and isinstance(v, int) == True:
        return True
    else:
        return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) \
            and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)

while True:
    print(msg_0)
    calc = input().split()
    x, oper, y = calc[0], calc[1], calc[2]
    try:
        if x != 'M':
            x = float(x)
        else:
            x = memory
        if y != 'M':
            y = float(y)
        else:
            y = memory
    except ValueError:
        print(msg_1)
        continue

    check(x, y, oper)

    if oper in operators:
        if oper == '+':
            result = float(x) + float(y)
        elif oper == '-':
            result = float(x) - float(y)
        elif oper == '*':
            result = float(x) * float(y)
        elif oper == '/':
            if y != 0:
                result = float(x) / float(y)
            else:
                print(msg_3)
                continue
        print(result)

        print(msg_4)
        store_result = input()
        if store_result == 'y':
            memory = result

        print(msg_5)
        continue_calc = input()
        if continue_calc == 'y':
            continue
        elif continue_calc == 'n':
            break
    else:
        print(msg_2)
 

