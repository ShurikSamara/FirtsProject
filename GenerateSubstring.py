# Вывести все подстроки исходной строки sourceString
def generate_substring():
    sourceString = "Съешь ещё этих мягких французских булок, да выпей чаю"
    print(sourceString)
    startIndex = 0

    while startIndex < len(sourceString):
        print(sourceString[startIndex:len(sourceString)])
        startIndex += 1

    invertString = ''.join(reversed(sourceString))
    endIndex = 1

    while endIndex < len(invertString):
        print(invertString[0:endIndex])
        endIndex += 1
    print(invertString)


generate_substring()
