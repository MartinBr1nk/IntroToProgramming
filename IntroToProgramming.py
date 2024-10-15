import os
from tkinter import YES
os.system('mode con: cols=129 lines=36')
finalefile=open("Finale Story.txt","r")

score = 0
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
import time
import random
import achivements
import themasterplan
def print_slow(str):
    for letter in str:
        print(letter, end = "")
        time.sleep(random.uniform(0.01, 0.05))

def print_faster(str):
    for letter in str:
        print(letter, end = "")
        time.sleep(random.uniform(0.001, 0.0005))

os.system('mode con: cols=250 lines=180')
terminalbootup  = achivements.doster
terminalbootup

singingachievement = achivements.singitloudandproud
thecoolname = achivements.yougotacoolname
lockallthedoorsmaybewellneverfindit = themasterplan.lockdownlogo
singitloud = themasterplan.masterplan
easteregginoctober = achivements.creatorwithnameofuser
netherdidithoughtwedgodown = achivements.weneedtogodeeper
mykola = achivements.errorface
tunnel = achivements.underground
theendgoose = achivements.gooseending
gooseascii = achivements.gooseinthewild

f = open("leaderboard.txt", "a") # this is the leaderboard for if you wish to see the scores

def goose_check():
    goose_message = ["Goose Not Detected", "Oie non détectée",
                     "Gans nie opgespoor nie", "Gans niet gedetecteerd", ":(",
                     "Wiżż mhux Individwat", "Oca non rilevata",
                     "Gèadh nach deach a lorg.", "Where is my Goose?",
                     "To Honk, Or not to Honk. That is the Question", "Knife",
                     "Wings of Fury will be unleashed upon you.",
                     "The Gaggle Shall Decide your Fate.",
                     "We Shall punish you to the furthest extent of the Law.",
                     "You will Be Tortured until you release him.",
                     "Watch it.", "We Shall Riot Outside until he is safe"]
    path = './Goose.png'
    gcheck = os.path.isfile(path)
    if gcheck == False:
        while True:
            print(goose_message[random.randint(0, 16)])
            time.sleep(1)
            print("\n")
    elif gcheck == True:
        print("Goose Detected. Launcing Software")

    #If the goose is NOT present then the program WILL NOT WORK.
    #DO NOT REMOVE THIS CODE. THE PROGRAM WILL NOT WORK WITHOUT IT.
goose_check()
print("Terminal Assistant -Last Updated- Jan 24th 1963")
nameplease= input("Input Agent Name ").upper()

if nameplease =="":
    nameplease = "USER"
    print("no name inputted. USER Is Default Name")

print("Please Be Aware that if there is a Yes or No Question," 
      " Please Enter yes or no.")

if nameplease =="MARTIN":
    thecoolname = True
    print("cool name dude!")
    print(easteregginoctober)
    time.sleep(10)
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
while message_loop == True:
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
    
    elif incomingmessage == "SKIP":
        devname = input("debug mode - enter dev name to continue")
        if devname == "Martin":
            message_loop = False
            print("skipping this dialogue.")
        elif devname != "Martin":
            print("wrong name detected.")


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
                    print("you have descended doors down to Floor 9"
                    "You check the room assigned in the terminal and look into it. "
                    "There is nothing but a New Terminal with Red Tape Keeping the Screen in Place. "
                    "You Check If the other doors are locked which they are. This allows you to continue to do your task."
                    "You started on the 8th Floor."
                    "you have gone down the steps and on a new floor."
                    "You check the room you chose on the list."
                    "There is a Sticky Note on the Desk. "
                    "You Check If the other doors are locked which they are. This allows you to continue to do your task.")
                    floor = floor + 1
                    doors = doors + 1
                    door3 = True
                    print("you are on floor", floor)
                    readnote = input("do you read the note?").upper()
                    if readnote == "YES":
                        print("The note says - This Terminal Has Passed Health And Safety tests")
                    elif readnote == "NO" or readnote == "":
                        print("you choose not to read the note")
                    else:
                        print("invalid input.")
                    logonterminal = input("will you log onto the terminal?").upper()
                    if logonterminal == "YES":
                        print_slow("Hello and Welcome Back to the terminal. What Would You Like to Do?")
                    elif logonterminal =="NO" or readnote == "":
                        print("you go back to the main hall to see what you can do")
                    total = total + 1
                    score = score + 500

                        
            
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
                        total = total + 1

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
                            littledoyouknow = input("let me ask you one more time. wake him up. Yes. Or. No.").upper()
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
                        elif geton == "NO" or geton == "":
                            print("okay then, you die because")
                            print("you dont want to play my game!")
                            life = life - 1
                        print("\n you walk through the station. as you do you see "
                              "that there is a sort of sign which says way out "
                              "so you then continue to walk down the corridor "
                              "which says way out on it and you see some "
                              "esculators. Do you go up them or no?")
                        esculator = input("go up esculator?")
                        if esculator == "yes":
                            print("so you decide to go up the esculator! as"
                                  " you continue up the esculator you see"
                                  " many adverts from throughout the years"
                                  " and then you get to the top of the esculator."
                                  " when you step off the esculator there is a "
                                  " shop. would you like to take some items?")
                            shop=input("welcome to my shop! what do you want"
                                       "i have cornettos, and a goose and"
                                       "i also have an apple crumble")
                            if shop == "cornetto":
                                print("good luck escaping those killers then..")
                                print(" and escape them you did. you ran,"
                                      " ran and ran some more. until you"
                                      " ended far far far away from"
                                      " that horrid place")
                                life = life - 1
                                score = score + 250
                            
                            elif shop == "goose": #one way to get good ending (goose ending)
                                print("honk! thank you for your purchase, hes"
                                      " been driving me up the walls lately!")
                                inspectgoose = input(" care to inspect inspect my goose?")
                                if inspectgoose == "yes":
                                    print("goose is big. 5ft with big wingspan"
                                          " very big and cool")
                                    print("you put a saddle on the goose and"
                                          " you break out of the station and"
                                          " you leave for pastures new.")
                                    print("the gaggle is now reunited! :D")
                                    life = life - 1
                                    theendgoose = True
                                    os.startfile("Goose.png")
                                    os.startfile("Angry Goose.png")
                                    os.startfile("Friendly Goose.png")
                                    os.startfile("Gallagher Goose.png")
                                    os.startfile("Old Goose.png")
                                    score = score + 90053
                                    break
                            
                            elif shop == "apple crumble":
                                print("you eat the apple crumble! it is very "
                                      "tasty. it reminds you of home")
                                print("in wizard of oz style you close your eyes"
                                      " and think of your home and then...."
                                      " you are home! ")
                                life = life - 1
                                score = score + 200
                                break

                        elif esculator != "yes":
                            print("your journey ends here noble agent.")
                            life = life - 1

                elif pickadoor == "2" and door2 == True:
                    print("you cannot go here! you have been here before")

                elif pickadoor == "2" and door2 == False: #door 2
                    print("you enter this room which is a very small room. ")
                    print("you look around, it looks like an office setup.")
                    print("the lock is broken. this means that the door doesn't close.")
                    print("Luckily there are tools on the desk to help you fix it.")
                    whichwire = input("do you join the blue with the red or blue?").upper()

                    if whichwire == "BLUE":
                        print("Congratulations!you're not as dumb as you seem")
                        print("well! you fixed the keycard reader!")
                        print("you have now locked the doors properly.")
                        doors = doors + 1
                        door2 = True
                    else:
                       print("you died because you are stupid.")
                       life -= 1
                       break
        
        elif whichone == "2": #farming! DONE
            print("you go to the open space which has lights on 24/7. ")
            print("there are different crops available to harvest: ")
            print("Corn, Potato, Carrot, Lettuce")
            print("Cabbage, Tomato, Pumpkin, Watermelon, Onion and Strawberry")
            harvestmoon = input("what would you like to harvest?" 
                                "(0 to end) ").upper()
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
                    score = score + 25
                    print("you have succesfully harvested a crop")
                    cropamount = cropamount + 1
                    harvestmoon = input("keep harvesting or press 0 to stop").upper()
                    print(harvestmoon)
                    print("you have successfully harvested", cropamount,"crops")
                else:
                    print("invalid data type. You have harvested nothing")
                    print("total amount of crops you have harvested is", cropamount)
                    harvestmoon = input("keep harvesting or press 0 to stop").upper()

        elif whichone == "3": #lockdown protocol if you dont put on the respirator you die
            lockthatdown=input("Please Enter your Name to Initiate Lockdown Protocol").upper()
            if lockthatdown == nameplease:
                print("Oxygen Deprivation Protocol has Started.")
                lockdownprotocol = True
                print_faster(lockallthedoorsmaybewellneverfindit)
            elif lockthatdown != nameplease:
                print("Lockdown cancelled.")
                total = total + 1

            if lockdownprotocol == True:
                lifeordeath = input("do you put on your respirator?").upper() #respirator
                if lifeordeath == "YES":
                    print("you are now breathing from the respirator. ")
                elif lifeordeath == "NO":
                    print("you start to feel light headed and suddenly, nothing.") 
                    print("You have passed out and in that time you have died.")
                    life=life -1
                    print_slow("Logging off - User Has Died")
        
        elif whichone == "4": #armory with prompt to fight an "intruder"
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
                total = total + 1
            elif fighthim == "yes" and pickaweapon == "2":
                print("he runs towards you at a speed, you then hit him"
                      " he is then stone cold and you then finish the job")
                total + 1
            elif fighthim == "yes" and pickaweapon == "3":
                print("in true style you hit him repeatedly until he falls"
                      "strange too because im sure i heard dont stop me now....")
                total = total + 1
                score = score + 650
            elif fighthim == "no":
                print("oh so your a pacifist? yeah no you're dead")
                life = life - 1
                
        
        elif whichone == "5": #avoid taxes
            print("taxes avoided")
            taxesavoided = taxesavoided + 1
            total + 1
            score = score + 250
            if taxesavoided == 5:
                print("authorities have been notified and you can no longer use this terminal.")
                break

        elif whichone == "6" and yougodown ==False: #checking if you went back up instead of doing the secret ending
            print("welcome to the message hub")
            print("you have no new messages")
            total + 1
        
        elif whichone == "6" and yougodown == True: #same as above
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
                total + 1
                score = score + 125


        elif whichone == "7": #number picking game 
            print("Let's play a magic game!")
            higherorlower = random.randint(1, 100)
            guess = 0
            while guess != higherorlower:
                try:
                    guess = int(input("what number will you guess 1 - 100"))
                    if guess > higherorlower:
                         print("too high!")
                         youguess = youguess + 1
                    elif guess < higherorlower:
                         print("too low!")
                         youguess = youguess + 1
                    else:
                         print("you got the number correct!")
                         print("you did it in", youguess, "tries")
                         score = score + 100
                         total = total + 1
                
                except TypeError:
                    print("thats not a single whole number IDIOT")
                else:
                    pass
        else:
            print("Invalid Option. Please enter a number between one and seven.")

        
        if total >= 7: #main ending 
            print(finalefile.read())
            life = life - 1

        finalefile.close()

print_slow("Systems Shutting Down....... \n")
print("You Achieved, Coolname =", thecoolname , "singitloud = ",singingachievement, "goose ending = ",theendgoose)
print("your score was", score)

addtotheboard = input("would you like to add your name and score to the leaderboard?").upper()
if addtotheboard == "YES":
    boardfile=open("Leaderboard.txt", "a")
    boardfile.write(f"\n {nameplease} - score = {score} \n achievements are : Coolname {thecoolname}, Singitloud {singingachievement}, Goose Ending {theendgoose}",)
    boardfile.close()
    
    boardfile = open("Leaderboard.txt", "r")
    print(boardfile.read())
    boardfile.close()
else:
    print("You did not say yes so the code will now exit. Thanks for playing!")
if theendgoose == True:
    print(gooseascii)

