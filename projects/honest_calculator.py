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

            while True:
                print(msg[4])  # "Do you want to store the result? (y / n):"
                ans = input()
                if ans == 'y': # Add additional flowchart logic here
                    memory = result
                    break
                elif ans == 'n':
                    break
            
            while True:
                print(msg[5])  # "Do you want to continue calculations? (y / n):"
                cont_calc = input()
                if cont_calc in ['n', 'y']:
                    break
            
            if cont_calc == 'n':
                break
            else:
                continue
        else:
            # "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
            print(msg[2])
            continue
 

