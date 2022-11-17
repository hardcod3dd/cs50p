camelize = input("camelcase : ").strip()

for letter in camelize:
    if letter.isupper():
        print("_" + letter.lower() , end="" )
    else:
     print(letter, end="")
     