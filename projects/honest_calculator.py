# Honest Calculator

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
operators = ['+', '-', '*', '/']
memory = 0


while True:
    print(msg_0)
    equation = input().split()
    x, oper, y = equation[0], equation[1], equation[2]
    try:
        x = float(equation[0])
        y = float(equation[2])
        oper = equation[1]
    except ValueError:
        print(msg_1)
        continue # to the next lines of code

    if oper not in operators:
        print(msg_2)
        continue # to the next lines of code

    if oper == '+':
        print(x + y)
        break # the loop and end program
    elif oper == '-':
        print(x - y)
        break # the loop and end program
    elif oper == '*':
        print(x * y)
        break # the loop and end program
    elif oper == '/' and y != 0:
        print(x / y)
        break
    else:
        print(msg_3) # go back to loop start
        
print("Out of loop")

