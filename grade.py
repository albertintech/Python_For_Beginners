grade = int(input())
max_score = int(input())
percent = (grade / max_score) * 100

if percent >= 90:
    print("A")
elif percent >= 80:
    print("B")
elif percent >= 70:
    print("C")
elif percent >= 60:
    print("D")
else:
    print("F")
