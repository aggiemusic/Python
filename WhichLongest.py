#Find the longest of two strings
wordA = input("Enter the first word: ")
wordB = input("Enter the second word: ")

if len(wordA) > len(wordB):
    print("The longer word is {0}".format(wordA))
elif len(wordB) > len(wordA): 
    print("The longer word is {0}".format(wordB))
else:
    print("It's a tie!")
        
        
        
        
        

