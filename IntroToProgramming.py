﻿total = 0
life = 1
floor = 8
lockdownprotocol = False
cropamount = 0


import time, random,achivements, themasterplan
def print_slow(str):
    for letter in str:
        print(letter, end = "")
        time.sleep(random.uniform(0.01, 0.05))

def print_faster(str):
    for letter in str:
        print(letter, end = "")
        time.sleep(random.uniform(0.001, 0.0005))


lockallthedoorsmaybewellneverfindit = themasterplan.lockdownlogo
singitloud = themasterplan.masterplan
terminalbootup  = achivements.doster

terminalbootup


print("Terminal Assistant -Last Updated- Jan 24th 1963")
nameplease= input("Input Agent Name ").upper()
if nameplease =="MARTIN":
    yougotacoolname = True
    print("cool name dude!")
    print(yougotacoolname)
print("Hello", nameplease, "You have been granted the highest level of authorisation  ") 
incomingmessage = input("incoming message from UNKNOWN - Origin HOMEBASE, REDACTED. Accept? Y/N").upper()
if incomingmessage == "Y":
        print_slow("Connection Secured. This is Captain REDACTED. We regret to inform you that your base has been comprimised. Please follow the measures in the next transmission. CONNECTION TERMINATED ")
elif incomingmessage == "N":
        print("You hear a noise coming from above you. Curious you leave the secure room and investigate, An Intruder then with a machete beheads you and it is game over.")
        life = 0
while life == 1:       
        print_slow("\n Please Do the following in any order: 1. Lock All The Doors 2. Harvest Crops 3. Initiate Oxygen Deprivation Protocol 4. Lock The Armoury 5. Avoid taxes 6. Check Camera 7. Play a Game! ")
        whichone = input ("what will you do first? enter any number")
        if whichone == "1":
            pickadoor = input("which door do you check? Door One: Past the Corridor, Door Two: Infront of you, Door Three: Down to The 9th Floor")
            if pickadoor == "3": #you go down a floor and then turn on a computer
                print("you have descended doors down to Floor 9. You started on the 8th Floor and now you have descended down the steps and into the new floor with 4 rooms. You check the room assigned in the terminal and look into it, There is nothing but a New Terminal with Red Tape Keeping the Screen in Place. There is a Sticky Note on the Desk")
                floor = floor + 1
                readnote = input("do you read the note?")
                if readnote == "yes":
                    print("The note says - This Terminal Has Passed Health And Safety tests")
                    print_faster(r"""   ______________
                                       /             /|
                                      /             / |
                                     /____________ /  |
                                    | ___________ |   |
                                    ||           ||   |
                                    ||  BOOT UP  ||   |
                                    || INITIATED ||   |
                                    ||___________||   |
                                    |   _______   |  /
                                   /|  (_______)  | /
                                  ( |_____________|/
                                   \
                                .=======================.
                                | ::::::::::::::::  ::: |
                                | ::::::::::::::[]  ::: |
                                |   -----------     ::: |
                                `-----------------------'""")
                    logonterminal = input("will you log onto the terminal?")
                    if logonterminal == "Y":
                        print_slow("Hello", nameplease, "Welcome Back to the terminal. What Would You Like to Do?")
                        print(pickadoor)
            elif pickadoor == "1": #Creator Decided to Put the masterplan by oasis in as the song you sing 
                print("Down the corridor you go! as you keep going down the corridor you contemplate whether you sing a little song or not.")
                sing = input("do you sing?")
                if sing =="yes":
                    print("so you have decided to sing! so you sing the masterplan by oasis and you say:")
                    print_slow(singitloud)
            elif sing =="no":
                print("well. you are no fun.")
                print("mr boring man continues to walk down until he reaches the corridor and then see")
                youdidntsing = True
        
        if whichone == "2": #farming! coming probably not soon
            print("you go to the open space which has lights on 24/7 to simulate daytime, there are different crops available to harvest: Corn, Potato, Carrot, Lettuce, Cabbage, Tomato, Pumpkin, Watermelon, Onion and Strawberry ")
            harvestmoon = input("what would you like to harvest? (0 to end) ").upper()
            while harvestmoon != "0": 
                if harvestmoon =="CORN" or harvestmoon =="POTATO" or  harvestmoon == "LETTUCE" or harvestmoon == "CABBAGE" or harvestmoon == "TOMATO" or harvestmoon == "PUMPKIN" or harvestmoon == "WATERMELON" or harvestmoon == "ONION" or harvestmoon == "STRAWBERRIES":
                    print("you have succesfully harvested a crop")
                    cropamount = cropamount + 1
                    harvestmoon = input("keep harvesting or press 0 to stop")
                    print(harvestmoon)
                    print("you have successfully harvested", cropamount,"crops")
                else:
                    print("invalid data type. You have harvested nothing")
                    print("total amount of crops you have harvested is", cropamount)
                    harvestmoon = input("keep harvesting or press 0 to stop")

        if whichone == "3": #lockdown protocol which so far doesnt do anything
            lockthatdown=input("Please Enter your Name to Initiate Lockdown Protocol").upper()
            if lockthatdown == nameplease:
                print("Oxygen Deprivation Protocol has Started.")
                lockdownprotocol = True
                print_faster(lockallthedoorsmaybewellneverfindit)

            lifeordeath = input("do you put on your respirator? it is a small device that will allow you to continue to be able to breathe. without it you could pass out ")