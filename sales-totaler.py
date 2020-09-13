inputFileName = input("Enter the file name: ")
outputFileName = input("Enter the name to write file to: ")

inFile = open( inputFileName, "r")
outFile = open (outputFileName, "w")

octSalesData = inFile.readlines()




for sales in octSalesData:
    splitSales = sales.split(" ")
    sale1 = splitSales[0]
    sale2 = splitSales[1] 
    sale1 = sale1[1: ]
    sale2 = sale2[1:-1]
    num1 = eval(sale1)
    num2 = eval(sale2)
    rowTotal = num1 + num2
    #print("$", num1,"    $  ", num2,"   $  ", rowTotal,file=outFile)
    print("${0:10.2f}".format(num1), "${0:10.2f}".format(num2), "${0:10.2f}".format(rowTotal), file=outFile) 

inFile.close()
outFile.close()





print("Done writing totals to 17-oct-total.txt")




    