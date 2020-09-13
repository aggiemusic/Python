#how to handle errors
try: 
    p1_X = int(input("Enter p1_x value: "))
    p1_Y = int(input("Enter p1_Y value: "))

    print ("") #just prints a blank space to for readability 

    p2_X = int(input("Enter p2_x value: "))
    p2_Y = int(input("Enter p2_Y value: "))


    slope = (p2_Y - p1_Y) / (p2_X - p1_X)

    print("The slope is {0:0.3f}.".format(slope))
except ZeroDivisionError:
    print("You entered in two x values that were the same")
except ValueError:
    print("You entered a value that is not a number")
    
    
