year = int(input("Provide a four digit year: "))

def div_by_4(year):
    if year % 4 == 0:
        return True

def not_div_by_100(year):
    if year % 100 != 0:
        return True


def div_by_400(year):
    if year % 400 == 0:
        return True

if div_by_4(year):
    if not_div_by_100(year):
        print("Leap")
    elif div_by_400(year):
        print("Leap")
    else:
        print("Ordinary")
else:
    print("Ordinary")
