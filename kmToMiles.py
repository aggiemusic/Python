kmValue = float(input('Enter the distance in km: '))
milesValue = kmValue / 1.609

if kmValue >= 0:
    milesValue = kmValue / 1.609
    print("{0:0.2} km is the same as {1:0.2f} mi.".format(kmValue, milesValue))
else: 
#if kmValue < 0:
    print("You cannot enter a negative km value")

print("Thanks for converting")



    