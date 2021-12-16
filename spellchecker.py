dictionary = ["aa", "abab", "aac", "ba", "bac", "baba", "cac", "caac"]

word = input("Enter some combination of a,b,c letters not more than 4 characters long and I will check if it is in the dictionary: ")

result = "In the dictionary" if word in dictionary else "Not in the dictionary"

print(result)
