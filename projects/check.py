# Honest Calculator

# msg_0 = "Enter an equation"
# msg_1 = "Do you even know what numbers are? Stay focused!"
# msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
# msg_3 = "Yeah... division by zero. Smart move..."
# msg_4 = "Do you want to store the result? (y / n):"
# msg_5 = "Do you want to continue calculations? (y / n):"
msg = ""
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = " You are"
operators = ['+', '-', '*', '/']
memory = 0


def is_one_digit(v):
    if v > -10 and v < 10 and isinstance(v, int) == True:
        return True
    else:
        return False

def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = "You are" + msg_6
    elif (v1 == 1 or v2 == 1) and v3 == "*":
        msg = "You are" + msg_7
    elif (v1 == 0 or v2 == 0) \
            and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = "You are" + msg_8
    elif msg != "":
        msg = "You are ... very, very lazy"
    print(msg)


x = 4
oper = "*"
y = 5.5

check(x, y, oper)

