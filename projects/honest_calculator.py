msg = [
    "Enter an equation",
    "Do you even know what numbers are? Stay focused!",
    "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
    "Yeah... division by zero. Smart move...",
    "Do you want to store the result? (y / n):",
    "Do you want to continue calculations? (y / n):",
    " ... lazy",
    " ... very lazy",
    " ... very, very lazy",
    " You are",
    "Are you sure? It is only one digit! (y / n)",
    "Don't be silly! It's just one number! Add to the memory? (y / n)",
    "Last chance! Do you really want to embarrass yourself? (y / n)"
]
operators = ['+', '-', '*', '/']
memory = 0

def is_one_digit(v):
    if (v > -10 and v < 10) and (v - int(v) == 0):  # ex 5.0 - 5 = 0
        return True
    else:
        return False

def check(v1, v2, v3):
    _msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        _msg = _msg + msg[6]  # "  ... lazy"
    if (v1 == 1 or v2 == 1) and v3 == "*":
        _msg = _msg + msg[7]  # " ... very lazy"
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        _msg = _msg + msg[8]  # "... very, very lazy"
    if _msg != "":
        _msg = msg[9] + _msg  # "You are" + prior msg
        print(_msg)

while True:
    print(msg[0])
    calc = input().split()
    x, oper, y = calc[0], calc[1], calc[2]

    if x == "M":
        x = memory
    if y == "M":
        y = memory

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg[1])  # "Do you even know what numbers are? Stay focused!"
        continue
    else:
        if oper in operators:
            check(x, y, oper)
            if oper == '+':
                result = float(x) + float(y)
            elif oper == '-':
                result = float(x) - float(y)
            elif oper == '*':
                result = float(x) * float(y)
            elif oper == '/' and y != 0:
                result = float(x) / float(y)
            else:
                print(msg[3])  # "Yeah... division by zero. Smart move..."
                continue
            print(result)

            stop = True
            while stop:
                print(msg[4])  # "Do you want to store the result? (y / n):"
                ans = input()
                if ans == 'y' and is_one_digit(result) != True:
                    memory = result
                    break
                elif ans == 'y' and is_one_digit(result) == True:
                    msg_index = 10
                    stop = True
                    while stop:
                        print(msg[msg_index])
                        ans = input()
                        if ans == 'y' and msg_index < 12:
                            msg_index += 1
                            continue
                        elif ans == 'n':
                            stop = False
                        else:
                            memory = result
                            stop = False
                            continue
                else:
                    break

            # Re-enter program here from new flowchart
            while True:
                print(msg[5])  # "Do you want to continue calculations? (y / n):"
                ans = input()
                if ans in ['n', 'y']:
                    break
            
            if ans == 'n':
                break
            else:
                continue
        else:
            # "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
            print(msg[2])
            continue
 

