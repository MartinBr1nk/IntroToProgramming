total = 0
life = 1
floor = 8
lockdownprotocol = False
cropamount = 0
doors = 0

import time, random,achivements, themasterplan
def print_slow(str):
    for letter in str:
        print(letter, end = "")
        time.sleep(random.uniform(0.01, 0.05))

def print_faster(str):
    for letter in str:
        print(letter, end = "")
        time.sleep(random.uniform(0.001, 0.0005))

singingachievement = achivements.singitloudandproud
thecoolname = achivements.yougotacoolname
lockallthedoorsmaybewellneverfindit = themasterplan.lockdownlogo
singitloud = themasterplan.masterplan
terminalbootup  = achivements.doster
terminalbootup
easteregginoctober = achivements.creatorwithnameofuser
netherdidithoughtwedgodown = achivements.weneedtogodeeper

print("Terminal Assistant -Last Updated- Jan 24th 1963")
nameplease= input("Input Agent Name ").upper()
if nameplease =="MARTIN":
    thecoolname = True
    print("cool name dude!")
    print(easteregginoctober)
    print(thecoolname)
print("Hello",nameplease,"You have been given the highest level of authority")
#inpput of accepting comms or not
incomingmessage = input("incoming message - Origin HOMEBASE. Accept?").upper()
if incomingmessage == "Y":
        print_slow("Connection Secured.")
        print_slow("Greetings Agent, This is Captain C.Stephens. ")
        print_slow("We regret to inform you that your base has been comprimised.") 
        print_slow("Please follow the measures in the next transmission. ")
        print_slow("CONNECTION TERMINATED ")
elif incomingmessage == "N":
        print("You hear a noise coming from above you. Curious you leave the secure room and investigate, An Intruder then with a machete beheads you and it is game over.")
        life = 0
while life == 1:       
        print_slow("\nPlease Do the following in any order: \n") 
        print("1. Lock All The Doors 2. Harvest Crops 3. Initiate Oxygen Deprivation Protocol")
        print("4. Lock The Armoury 5. Avoid taxes 6. Check Comms 7. Play a Game! ")
        whichone = input ("what will you do first? enter any number")
        if whichone == "1":
            while doors != 3:
                pickadoor = input("what do you check first? Door 1, Door 2 or Door 3") #Prompt asking you which floor to go to
            
                if pickadoor == "3": #you go down a floor and then turn on a computer
                    print("you have descended doors down to Floor 9")  
                    print("You check the room assigned in the terminal and look into it. ")
                    print("There is nothing but a New Terminal with Red Tape Keeping the Screen in Place. ")
                    print("You Check If the other doors are locked which they are. This allows you to continue to do your task.")
                    print("You started on the 8th Floor.")
                    print("you have gone down the steps and on a new floor.")
                    print("You check the room you chose on the list.") 
                    print("There is only a Terminal with Tape Keeping the Screen in. ")
                    print("There is a Sticky Note on the Desk. ")
                    print("You Check If the other doors are locked which they are. This allows you to continue to do your task.")
                    floor = floor + 1
                    doors = doors + 1
                    print("you are on floor", floor)
                    readnote = input("do you read the note?")
                    if readnote == "yes":
                        print("The note says - This Terminal Has Passed Health And Safety tests")
                    logonterminal = input("will you log onto the terminal?").upper()
                    if logonterminal == "YES":
                        print_slow("Hello and Welcome Back to the terminal. What Would You Like to Do?")
                        
            
                elif pickadoor == "1": #door 1/way to secret ending 
                    print("Down the corridor you go! as you keep going down the corridor you contemplate whether you sing a little song or not.")
                    sing = input("do you sing?")
                    if sing =="yes":
                        print("so you have decided to sing! so you sing the masterplan by oasis and you say:")
                        print_slow(singitloud)
                        singingachievement= True
                    elif sing =="no":
                        print("well. you are no fun.")
                        print("mr boring man continues to walk down the hall.") 
                        print("he then sees that there is only one door which is locked. ")
                        print("He puts the keycard to the door and as he has been given the highest clearance is through.") #door down to true ending 
                        youdidntsing = True
                    print("you go down a set of stairs taking you back in time into a place which looks very dated.")
                    floor = floor + 1942
                    doors = doors + 1
                    print("You are on an unknown floor. You try to see what floor you are at on the sign but it is illegible. ")
                    print("The room looks like a train station ")
                    iwantmymoneyback = input("do you go back upstairs or do you stay?").upper()
                    if iwantmymoneyback == "LEAVE":
                        print("You decide to not do this and go straight upstairs because this is not worth your time")
                        floor = floor - 1942
                        print("you are back on floor", floor)
                    elif iwantmymoneyback == "STAY": 
                        print("so you decided to venture forth! you are not the coward i thought you would be. here you earned this little achievement my treat.")
                        netherdidithoughtwedgodown == True
                        print("as you walk past all the debris in this abandoned station-like immitation.")
                        print("you notice there seems to be a fellow worker sitting.")
                        littledoyouknow = input("do you wake him up?").upper()
                        while littledoyouknow != "YES":
                            print("You dont have a choice. You said,",littledoyouknow,)
                            littledidyouknow = input("let me ask you one more time. wake him up. Yes. Or. No.").upper()

                elif pickadoor == "2": #door 2
                    print("you enter this room which is a very small room. ")
                    print("you look around, it looks like an office setup.")
                    print("the lock is broken. this means that the door doesn't close.")
                    print("Luckily there are tools on the desk to help you fix it.")
                    whichwire=input("do you join the blue with the red or blue?").upper
                    if whichwire == "BLUE":
                        print("Congratulations! you aren't as dumb as you look")
                    elif whichwire == "RED":
                        print("did you honestly think blue goes with red?")
                        life = life - 1
                    if life == 1:
                        print("well! you fixed the keycard reader!")
                        print("you have now locked the doors properly.")
                        doors = doors + 1
        
        if whichone == "2": #farming! coming probably not soon
            print("you go to the open space which has lights on 24/7. ")
            print("there are different crops available to harvest: ")
            print("Corn, Potato, Carrot, Lettuce")
            print("Cabbage, Tomato, Pumpkin, Watermelon, Onion and Strawberry")
            harvestmoon = input("what would you like to harvest? (0 to end) ").upper()
            while harvestmoon != "0": 
                if harvestmoon =="CORN"\
                   or harvestmoon =="POTATO" \
                   or  harvestmoon == "LETTUCE" \
                   or harvestmoon == "CABBAGE" \
                   or harvestmoon == "TOMATO" \
                   or harvestmoon == "PUMPKIN" \
                   or harvestmoon == "WATERMELON" \
                   or harvestmoon == "ONION" \
                   or harvestmoon == "STRAWBERRY"  \
                   or harvestmoon == "CARROT":
                    print("you have succesfully harvested a crop")
                    cropamount = cropamount + 1
                    harvestmoon = input("keep harvesting or press 0 to stop").upper()
                    print(harvestmoon)
                    print("you have successfully harvested", cropamount,"crops")
                else:
                    print("invalid data type. You have harvested nothing")
                    print("total amount of crops you have harvested is", cropamount)
                    harvestmoon = input("keep harvesting or press 0 to stop").upper()

        if whichone == "3": #lockdown protocol which so far doesnt do anything
            lockthatdown=input("Please Enter your Name to Initiate Lockdown Protocol").upper()
            if lockthatdown == nameplease:
                print("Oxygen Deprivation Protocol has Started.")
                lockdownprotocol = True
                print_faster(lockallthedoorsmaybewellneverfindit)

            lifeordeath = input("do you put on your respirator?").upper()
            if lifeordeath == "YES":
                print("you are now breathing from the respirator. ")
            elif lifeordeath == "NO":
                print("you start to feel light headed and suddenly, nothing.") 
                print("You have passed out and in that time you have died.")
                life=life -1
                print_slow("Logging off - User Has Died")
print_slow("Systems Shutting Down....... \n")
print("You Achieved, Coolname =", thecoolname , "singitloud = ",singingachievement)
