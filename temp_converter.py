for tempConversions in range(3): 
    inputFahrenheitString = input("Enter the temp in F: ")
    tempinF = float(inputFahrenheitString)
    tempinC = ((tempinF -32) * 5/9)
    print( "The temperature in C is", tempinC, "degrees" ) 