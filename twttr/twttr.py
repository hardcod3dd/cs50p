wovels = ["a","e","u","i","o"]

tweet = input("Input: ")
for letter in tweet:
    if letter.lower() in wovels:
        print("" , end="")
    else:
        print(letter , end="")