def main():
    toConvert = input("What time is it ? \n")
    converted = convert(toConvert)



    if 7.00 <= converted <= 8.00:
        print("breakfast time")
    elif 12.00 <= converted <= 13.00:
        print("lunch time")
    elif 18.00 <= converted <= 19.00:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes) / 60
    toReturn = hours + minutes
    return float(toReturn)

if __name__ == "__main__":
    main()