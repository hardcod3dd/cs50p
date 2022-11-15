answer = input("give me the answer for the Great Question of Life: \n").lower().strip()

if answer == "42":
    print("yes")
elif answer == "forty two":
    print("yes")
elif answer == "forty-two":
    print("yes")
else:
    print("no")