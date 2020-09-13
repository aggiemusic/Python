#Given  numbers, find the max value - Sentinel Loop example 
#numofValues = int(input("Enter the number of values: "))

sentienlValue = -1

#POST 
nextValue = int(input("Enter a value: "))
#FENCE
maxValue = nextValue 
while nextValue != sentienlValue:
    #POST
    nextValue = int(input("Enter the next value: "))
    #FENCE
    if nextValue > maxValue:
        maxValue = nextValue
        
if maxValue == sentienlValue:
    print("No values entered") 
else: 
    print("The max value is {0}".format(maxValue))
    

