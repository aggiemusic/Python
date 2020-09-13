from random import randrange

print("This program rolls two 6-sided dice until their sum is a given target value")

targetValue = int(input("Enter the target sum to roll for: "))

def main():
       
    sumOfRolls = 0
    count = 1
    
    while sumOfRolls != targetValue:
        dieA = randrange (1, 7)
        dieB = randrange (1, 7)
        sumOfRolls = dieA + dieB
        print("Roll: {} and {}, sum is {}".format(dieA, dieB, sumOfRolls))
        if sumOfRolls == targetValue:
            print("You got it in {} rolls!".format(count))     
        count = count + 1
             
main()



