
accepted = [5,10,25]
due = int("50")

while due > 0:
    print("Amount due: " , due)
    coins = int(input("Insert Coin: "))
    if coins in accepted:
        due -= coins

print("Change owed" , str(due).strip("-"))

