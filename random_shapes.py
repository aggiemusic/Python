import random
from random import randrange

#Get a user input file name 
fileName = input("Enter the drawing file name to create: ")
    
#a function to create a random circle. Using randrange() to randomly set the coordinates.  
def getRandomCircles(): #name,centerPt, radius,color
    name = 'Circle'
    centerPt = (random.randrange(30,450), random.randrange(30,450)) 
    radius = random.randrange(0,40) 
    red = random.randrange(0,85)
    green = random.randrange(86,156)
    blue = random.randrange(157,255)
    circleFormatting = "{}; {}, {}; {}; {}, {}, {}".format(name, centerPt[0], centerPt[1], radius, red, green, blue)
    writeToFile = open(fileName, 'a')
 
    print(circleFormatting, file = writeToFile)
  



#a function to create a random rectangle. Using randrange() to randomly set the coordinates
def getRandomRectangles(): 
    name = 'Rectangle'
    coordA = (random.randrange(20,500), random.randrange(20,500)) 
    coordB = (random.randrange(35,400), random.randrange(35,400)) 
    red = random.randrange(0,85)
    green = random.randrange(86,156)
    blue = random.randrange(157,255)
    rectangleFormatting = "{}; {}, {}; {}, {}; {}, {}, {}".format(name, coordA[0], coordA[1], coordB[0], coordB[1], red, green, blue)
 
    writeToFile = open(fileName, 'a')
 
    print(rectangleFormatting, file = writeToFile)
  
    
def main():
    #get number of shapes and loop for creating random shapes 
    
    numOfShapes = eval(input("Enter the number of shapes to make: "))



    for i in range(numOfShapes):
        x = random.randint(0,1)
        if x == 0:
            getRandomRectangles()
        else:
            getRandomCircles()
    
    
             
main()


    



               
            




    
    
                

