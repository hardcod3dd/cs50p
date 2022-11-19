def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):


    if 2 <= len(s) <= 6:
        if s.isalpha() and s.isupper():
            return True
        if s.isalnum() and s.isupper():
            if s[0:2].isalpha() and s[0:2] != "0":
                    if s[1:len(s) - 2].isalpha():
                        for i in range(len(s)):
                            if s[i].isnumeric():
                                if s[i] == "0":
                                    return False
                                else:
                                    return True



main()