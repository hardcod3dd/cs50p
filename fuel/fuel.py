
while True:
    try:
        x,y = input("Fraction: ").split("/")
        x = int(x)
        y = int(y)
        percent = (x/y)*100
        percent = round(percent)
        if 1 < percent < 99:
            print(f"{percent}%")
            break
        elif percent <= 1:
            print("E")
            break
        elif 100 >= percent >= 99:
            print("F")
            break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass