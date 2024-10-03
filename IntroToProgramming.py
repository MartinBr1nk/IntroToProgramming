total = 0
life = 1
floor = 8
lockdownprotocol = False
cropamount = 0
doors = 0
taxesavoided = 0
yougodown = False
youguess = 1

door2 = False
door3 = False

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
mykola = achivements.errorface
tunnel = achivements.underground

print("Terminal Assistant -Last Updated- Jan 24th 1963")
nameplease= input("Input Agent Name ").upper()

if nameplease =="":
    nameplease = "USER"
    print("no name inputted. USER Is Default Name")

if nameplease =="MARTIN":
    thecoolname = True
    print("cool name dude!")
    print(easteregginoctober)
    print(thecoolname)

elif nameplease == "MYKOLA":
    print(mykola) #if mykola plays, a photo of a parasaurolophus appears with his head on it.

elif nameplease == "JACK":
    print("WELCOME TO THE HELL EXPIDITION")
    print("Exiting Hell Expidition.")

print("Hello",nameplease,"You have been given the highest level of authority")
#inpput of accepting comms or not
incomingmessage = input("incoming message - Origin HOMEBASE. Accept?").upper()
message_loop = True
while message_loop:
    if incomingmessage == "YES":
            message_loop = False
            print_slow("Connection Secured.")
            print_slow("Greetings Agent, This is Captain C.Stephens. ")
            print_slow("We regret to inform you that your base has been comprimised.") 
            print_slow("Please follow the measures in the next transmission. ")
            print_slow("CONNECTION TERMINATED ")
    elif incomingmessage == "NO":
            message_loop = False
            print("You hear a noise coming from above you. Curious you leave the secure room and investigate, An Intruder then with a machete beheads you and it is game over.")
            life = life - 1
    else:
        print("input invalid dummy")
        incomingmessage = input("Accept or Deny the Intercom?").upper()
while life == 1:       
        print_slow("\nPlease Do the following in any order: \n") 
        print("1. Lock All The Doors 2. Harvest Crops 3. Initiate Oxygen Deprivation Protocol")
        print("4. Lock The Armoury 5. Avoid taxes 6. Check Comms 7. Play a Game! ")
        whichone = input ("what will you do first? enter any number")
        if whichone == "1":
            while doors != 3:
                pickadoor = input("what do you check first? Door 1, Door 2 or Door 3") #Prompt asking you which floor to go to
                if pickadoor == "3" and door3 == True:
                    print("you cannot go here!")

                elif pickadoor == "3" and door3 == False: #you go down a floor and then turn on a computer
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
                    door3 = True
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
                    elif sing =="no" or sing =="":
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
                    if iwantmymoneyback == "LEAVE" or iwantmymoneyback =="":
                        print("You decide to not do this and go upstairs because this is not worth your time")
                        yougodown = True
                        print(yougodown)
                        floor = floor - 1942
                        print("you are back on floor", floor)

                    elif iwantmymoneyback == "STAY": 
                        print("so you decided to venture forth!") 
                        print("you are not the coward i thought you would be.")
                        print("here you earned this achievement my treat.")
                        netherdidithoughtwedgodown == True
                        print("as you walk past this abandoned station")
                        print("you notice there seems to be a worker sitting.")
                        littledoyouknow = input("do you wake him up?").upper()

                        while littledoyouknow != "YES":
                            print("You dont have a choice. You said,",littledoyouknow,)
                            littledidyouknow = input("let me ask you one more time. wake him up. Yes. Or. No.").upper()
                        print("He jolts awake in a cold sweat.")
                        print("he seems rattled about where he is. ")
                        print("there is also a lot of blood on the floor")
                        print("he tells you things, interesting things. rouses")
                        print("he also tells you that his favourite flavour of")
                        print("oh wait no hes dead.")
                        print("you then walk through more. you see a carriage")

                        geton = input("get in carriage and go?").upper()
                        if geton == "YES":
                            print("and so you get on and flick the lever but")
                            print("no movement! you get off again")
                            print("you decide to look around. you see a PSU.")
                            turnon = input("turn on the PSU?").upper()
                            if turnon == "YES":
                                print("BOOM ITS ON!")
                                print("you get back into the carriage and go")
                                print_slow("\n Weeeeeeeeeeeeeeeeeeeeeeeeeeeee \n")
                                print("and you are at your destination!")
                                print("it is this old midpoint between stations")
                                print_faster(tunnel)
                        if geton == "NO":
                            print("okay then, you die because")
                            print("you dont want to play my game!")
                            life = life - 1

                if pickadoor == "2" and door2 == True:
                    print("you cannot go here! you have been here before")

                elif pickadoor == "2" and door2 == False: #door 2
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
                        door2 = True
        
        if whichone == "2": #farming! DONE
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

        if whichone == "3": #lockdown protocol if you dont put on the respirator you die
            lockthatdown=input("Please Enter your Name to Initiate Lockdown Protocol").upper()
            if lockthatdown == nameplease:
                print("Oxygen Deprivation Protocol has Started.")
                lockdownprotocol = True
                print_faster(lockallthedoorsmaybewellneverfindit)
            elif lockthatdown != nameplease:
                print("Lockdown cancelled.")

            if lockdownprotocol == True:
                lifeordeath = input("do you put on your respirator?").upper() #respirator
                if lifeordeath == "YES":
                    print("you are now breathing from the respirator. ")
                elif lifeordeath == "NO":
                    print("you start to feel light headed and suddenly, nothing.") 
                    print("You have passed out and in that time you have died.")
                    life=life -1
                    print_slow("Logging off - User Has Died")
        
        elif whichone == "4":
            print("you walk to the armory and decide you need a weapon")
            willyoutakeaweapon = input("will you take a weapon from the armoury?").upper()
            if willyoutakeaweapon == "YES":
                pickaweapon = input("pick a number between 1 and 3!")
                if pickaweapon == "1":
                    print("Aha! You have a medival broadsword! It has the engravings - MB - Maybe someone of great importance and maybe not.")
                elif pickaweapon =="2":
                    print("you have an arm? Not of human origin but a microphone arm, it has a thick metal bottom which might be of great use")
                elif pickaweapon == "3":
                    print("you get a cricket bat! where are the zombies and fences to jump over.....")
            print("as you are walking into your terminal you see a figure rush you")
            fighthim = input("do you fight the figure?")
            if fighthim == "yes" and pickaweapon == "1":
                print("you behead the intruder and spill his guts out")
            elif fighthim == "yes" and pickaweapon == "2":
                print("he runs towards you at a speed, you then hit him")
                print("he is then stone cold and you then finish the job")
            elif fighthim == "yes" and pickaweapon == "3":
                print("in true style you hit him repeatedly until he falls")
                print("strange too because im sure i heard dont stop me now....")
            elif fighthim == "no":
                print("oh so your a pacifist? yeah no you're dead")
                life = life - 1
        
        if whichone == "5":
            print("taxes avoided")
            taxesavoided = taxesavoided + 1
            if taxesavoided == 10:
                print("authorities have been notified and you can no longer use this terminal.")
                break

        if whichone == "6" and yougodown ==False:
            print("welcome to the message hub")
            print("you have no new messages")
        
        elif whichone == "6" and yougodown == True:
            print("you have a new message! Message from 2 mins ago.")
            readit =input("will you read the message?")
            if readit == "yes":
                print("hello,",nameplease,"I need your help and it is urgent.")
                print("the government is making a rouse. i promise you this.")
                print("the problem is that we are being intruded by soldiers")
                print("soldiers which are hired by the government!")
                print("go down to the bottom of those steps. ")
                print("there you can escape. godspeed",nameplease,".")
                doors = doors -1


        if whichone == "7":
            print("Let's play a magic game!")
        higherorlower = random.randint(1, 100)
        while True:
                try:
                    putanumberin = int(input("What number will you guess? "))
                    if putanumberin > higherorlower:
                        print("Too high!")
                        youguess = youguess +1
                    elif putanumberin < higherorlower:
                        print("Too low!")
                        youguess = youguess +1
                    else:
                        print("You win!")
                        print("it took you", youguess,"guesses!")
                        youguess = youguess - youguess
                        youguess = youguess + 1
                        break
                except ValueError:
                    print("Invalid input. Please enter a number.")


print_slow("Systems Shutting Down....... \n")
print("You Achieved, Coolname =", thecoolname , "singitloud = ",singingachievement)

