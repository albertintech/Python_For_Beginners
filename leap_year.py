year = int(input("Provide a four digit year: "))
a = 400

if year % 4 == 00 and year % 100 != 00 or year % a == 0:
    print("Leap")
else:
    print("Ordinary")
