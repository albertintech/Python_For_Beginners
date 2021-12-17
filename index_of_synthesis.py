# One way to classify the languages of the world is by looking at their morphological systems. One classification is based on the index of synthesis that reflects the average number of morphemes in a word. The values vary between 1 and 4 and there are 3 types of languages according to that system. Here they are:

# Type — Index

# Analytic — less than 2

# Synthetic — from 2 to 3 (inclusively)

# Polysynthetic — more than 3

# Write a program that given the index of synthesis determines the type of the language.

index = float(input())

if index < 2.0:
    print("Analytic")
elif index <= 3.0:
    print("Synthetic")
else:
    print("Polysynthetic")
