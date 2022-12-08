months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("enter: ").strip()
        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)
            if month <= 12 and day <= 31:
                print(f"{year}-{month:02}-{day:02}")
                break

        month, day, year = date.split(" ")
        if month.title() in months:
            if "," in day:
                day = int(day.strip(","))
                intMonth = int(months.index(month)) + 1
                if intMonth <= 12 and day <= 31:
                    print(f"{year}-{intMonth:02}-{day:02}")
                    break

    except (KeyError,ValueError):
        pass
    except EOFError:
        print("", end="\n")
        break
