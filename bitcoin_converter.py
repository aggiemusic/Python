print( "As of 1/15/20 at 3:07 PM Bitcoin is trading at $8745.69 per bitcoin" )
InputBitCoinString = input("Enter the bitcoin amount: ")
BitCoinAmount = float(InputBitCoinString)
AmountinDollars = BitCoinAmount * 8745.69
print( "That is worth", AmountinDollars, "us dollars" )