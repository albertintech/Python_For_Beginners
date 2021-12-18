msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"


memory = 0
plus = "+"
minus = "-"
multi = "*"
divide = "/"
operands = [plus, minus, multi, divide]

while True:
    calc = input(f"{msg_0} \n").split()

    try:
        if calc[0] == "M":
            calc[0] = memory
        elif calc[2] == "M":
            calc[2] = memory

        calc[0] = float(calc[0])
        calc[2] = float(calc[2])

        if calc[1] in operands:
            if calc[1] == plus:
                memory = calc[0] + calc[2]
                print(memory)
            elif calc[1] == minus:
                memory = calc[0] - calc[2]
                print(memory)
            elif calc[1] == multi:
                memory = calc[0] * calc[2]
                print(memory)
            elif calc[1] == divide:
                if calc[2] != 0:
                    memory = calc[0] / calc[2]
                    print(memory)
                else:
                    print(msg_3)
                    continue
            store = input(f"{msg_4} \n")
            if store == "y":
                pass
            elif store == "n":
                memory = 0
            again = input(f"{msg_5} \n")
            if again == "y":
                continue
            else:
                break

        elif calc[1] != any(operands):
            print(msg_2)
    except:
        print(msg_1)
