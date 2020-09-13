phraseToRepeat = input( "Input your phrase: ")
timesToRepeat = int(input("How many times should it be repeated: "))
for index in range(timesToRepeat):
    print(format(index + 1), phraseToRepeat) 
        