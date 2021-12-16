word_1 = "riddikulus"
word_2 = "alohomora"

# How many letters does the longest word contain?

if len(word_1) > len(word_2):
    print(len(word_1))
else:
    print(len(word_2))

# or
print(max(len(word_1), len(word_2)))
