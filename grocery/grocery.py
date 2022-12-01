foods = {}

while True:
    try:
        food = input().upper()
        if food not in foods:
            foods[food] = 1
        else:
            foods[food] += 1

    except KeyError:
        pass
    except EOFError:
        print("\n")
        sFoods = dict(sorted(foods.items()))
        for i in sFoods:
            print(sFoods[i], i)
        break
