def main():
    import math 
    print("This program will calculate the amount of filler needed")
    print()
    numberofballs = float(input("How any bowling balls will be manufactured?  "))
    balldiameter = float(input("What is the diameter of each ball in inches?  "))
    corevolume = float(input("What is the core volume in inches cubed?  "))
    radius = balldiameter / 2
    totalvolume = (4/3) * math.pi * (radius * radius * radius)
    tvlesscore = totalvolume - corevolume
    fillerneeded = tvlesscore * numberofballs
    print ()
    print("You will need", fillerneeded, "inches cubed of filler")
main()
