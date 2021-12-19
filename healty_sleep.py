# recommended hours of sleep per day
A = int(input())

# recommended hours of maximum sleep per day
B = int(input())

# actual sleep
H = int(input())

if H < A:
    print("Deficiency")
elif H > B:
    print("Excess")
else:
    print("Normal")    
