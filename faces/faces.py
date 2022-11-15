def convert(toConvert):
    toConvert = toConvert.replace(":)","🙂").replace(":(","🙁")
    return toConvert

def main():
    sentence = input("enter the sentence: \n")
    print(convert(sentence))

main()
