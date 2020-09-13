#Classic Movie Monster Adventure Game
#Ashley Music - Final Project 
import time
import random
import sys 
import graphics as g


def displayIntro(hero):#passing the hero object so the hero name can be formatted in the introduction
    """Creates the spooky introduction with an image to the Monster Movie Adventure Game. Using sleep so that all text doesn't pop up at once"""
    monsterIntroImage = 'Monster Intro.gif' #adding an image adds an extra creative touch that was not listed in the requirments
    win = g.GraphWin("Movie Monster Game", 400, 400)
    gameIntroImage = g.Image(g.Point(200,200), monsterIntroImage)
    gameIntroImage.draw(win)
    #print("Welcome to the Classic Movie Monsters Adventure Game {}!".format(hero.name))
    print("{}, you are a movie projectionist and a magician has put a spell on all of the classic movie monster films".format(hero.heroName))
    time.sleep(1)
    print("They have come to life and you must hunt them all down...")
    time.sleep(1)
    print("Before they hunt you!!!!") 
    time.sleep(1) 
    print("Collect 3 movie reels and make it to the projection room in 10 steps to reverse the spell!! Good luck!!")
    time.sleep(1)
    print(" ")
    print("*************************************************************************************************************")
    win.close()

class Hero:
    """Creates the hero class. Contains name, health and attack information"""
    def __init__ (self, heroName, heroAttack, heroHealth): 
        self.heroName = heroName
        self.heroAttack = heroAttack
        self.heroHealth = heroHealth 
             
    """The class methods that will be used when the hero is fighting monsters"""
   
    def getHeroHealth(self):
        return self.heroHealth  

            
    def setHeroHealth(self,x):
        self.heroHealth -= x 

        
    def heroAttack(self):
        self.heroAttack = heroAttack
        return self.heroAttack 
            
    def checkIfAlive(self):
        if self.heroHealth < 0:
            print("You have been killed!! You have 0 health points left. You lose all the movie reels you have collected to the monsters. They win this time!!")
            sys.exit()  #stops the script if the hero has been killed. Game over!  
        else:
            print("{}, you have survived the attack! Good job!".format(self.heroName))
            print(" ") 
            
        
class Monster:
    """Creates the monster parent class. Contains name, attack, health, intro and image information that is shared by all three monsters"""
    def __init__ (self, name, monsterAttack, monsterHealth, intro, image):
        self.name = name
        self.monsterAttack = monsterAttack
        self.monsterHealth = monsterHealth
        self.intro = intro
        self.image = image
        
    """The methods that are shared by all monsters. Used to provide an introduction and image of the monster. Also contains the methods needed for fighting the hero"""
        
    def getMonsterHealth(self):
        return (self.monsterHealth) 
            
            
    def setMonsterHealth(self, x):
        self.monsterHealth -= x 

    def MonsterAttack(self):
        self.monsterAttack = monsterAttack
        return self.monsterAttack 
            
                
    def getIntro(self):
        print(self.intro)
        
    def getImage(self): #adding an image adds an extra creative touch that was not listed in the requirments. Makes the fight more interesting.
        win = g.GraphWin("Monster!!", 450, 450)
        monsterImage = self.image
        filmReel = g.Image(g.Point(200,200), monsterImage)
        filmReel.draw(win)
        time.sleep(1.5)
        win.close()

                           
              
def getTrinket():   
    """The funtion to get a trinket. The hero must collect trinkets to win the game. Also contains a graphic image for the movie reels"""
    print("You have found a movie reel!")
    filmReelImage = 'FilmReel.gif'
    win = g.GraphWin("Movie Reel", 400, 400) #adding an image adds an extra creative touch that was not listed in the requirments. Makes finding the movie reel more interesting.
    filmReel = g.Image(g.Point(200,200), filmReelImage)
    filmReel.draw(win)
    time.sleep(1.5)
    win.close()
    
         
def getFight(dracula, wolfman, mummy, hero, randomMonster):#passing the monster objects and random monster list to the get fight function so the health points and list will update outside of the get fight loop
    """The fight funtion.  Allows for random monster selection and removes the random monster from the list if it has been killed by the hero"""
    selectedMonster = random.choice(randomMonster)     
    selectedMonster.getIntro()
    selectedMonster.getImage()
    print("You are being attacked by {}!".format(selectedMonster.name))
    print(" ")
    hero.setHeroHealth(selectedMonster.monsterAttack)
    time.sleep(.5)
    print("You have lost {} health points. {} health points left".format(selectedMonster.monsterAttack, hero.heroHealth))
    hero.checkIfAlive()
    print(" ")
    print("You are attacking {}".format(selectedMonster.name))
    print(" ") 
    selectedMonster.setMonsterHealth(hero.heroAttack)
    time.sleep(.5)
    print("You gave {} points worth of damage. {} has {} health points left.".format(hero.heroAttack, selectedMonster.name, selectedMonster.monsterHealth)) 
    if selectedMonster.monsterHealth < 0:
        print("{} has been killed!!!".format(selectedMonster.name))
        randomMonster.remove(selectedMonster)   #removes the monster from the list if they have been killed so you won't encounter the monster anymore
    else:
        print("{} has survived your attack!".format(selectedMonster.name))
    print(" ") 
        

        
def projectionRoom():
    """Function for making it to the projection room at the end of the 10 steps. The hero must make it here to win the game. Also contains an image that comes up when here gets here"""
    win = g.GraphWin("Projection Room", 450, 450) #adding an image adds an extra creative touch that was not listed in the requirments. Makes making it to the projection room more realistic.
    projectionRoomImage = 'Projection Room.gif'
    projectionRoom = g.Image(g.Point(200,200), projectionRoomImage)
    projectionRoom.draw(win)
    print("Congratulations! You have made it to the projection room!!")
    print("Let's hope you collected enough movie reels to put these monsters back where they belong... on film!!!")
    time.sleep(3)
    win.close()
        
def endGame(hero): #passing the hero object to the end game function so the healh points can be formatted 
    print("{}, you ended the game with {} health points".format(hero.heroName, hero.getHeroHealth())) 

                
def main():
    """The main game loop. Will display the intro, set up an empty trinket list to append to and count at the end of the game to see if the hero wins. Contains the loop
    to determine if the hero will collect a trinket or fight a monster."""
    dracula = Monster("Dracula", 15, 100,  "I'm Dracula and I've come to suck your blood!!", 'Dracula.gif')
    wolfman = Monster( "Wolfman",  10,  75, "I'm the Wolfman. I swear I am only bad when the moon is full!", 'Wolfman.gif')
    mummy = Monster( "Mummy", 5, 50,"I used to be a king! I will be a king once again and you can't stop me!", 'Mummy.gif')    
    heroName = input("Welcome to the Classic Movie Monster Adventure Game! Please enter your name:")
    hero = Hero( heroName,  15,  100) #stores the user input hero name
    displayIntro(hero) #allows the introduction to display the hero name 
    randomMonster = [dracula, wolfman, mummy]
    trinketList = []
    for steps in range(10):
        stepsLeft = 10 - steps  
        keepMoving = input("You have {} steps left. Would you like to step forward (y or n)?".format(stepsLeft))
        print(" ") 
        if keepMoving == 'n':
            break
        else:
            x = random.randint(0,1)   
            if x == 0:
                getTrinket()
                trinketList.append("Movie Reel")
                print(" ")
            else:
                getFight(dracula, wolfman, mummy, hero, randomMonster)
    print(" ")
    print("*******************************************************************************************************")
    print("*******************************************************************************************************")
    if keepMoving != 'n':    #if the hero doesn't stop moving they reach the projection room and their trinket list is counted
        projectionRoom()
        count = trinketList.count("Movie Reel") 
        if count >= 3:
            print("You win!!!. You have collected {} movie reels".format(count))       
        else:
            print("You did not collect enough movie reels to get the monsters back into their films. You lose. The monsters take over the theatre")
        endGame(hero)   
    else:
        print("You have decided to stop moving and drop any movie reels you might have collected. You lose. The monsters surround you...") #if the hero stops moving - they lose. 
    
    
         
main()














            

    


          

        
        
        
        
      
      





