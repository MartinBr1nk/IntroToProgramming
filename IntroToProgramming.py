total = 0
life = 1
floor = 8
lockdownprotocol = False
cropamount = 0

#Achievements!
singitloud = False
hungyforoxygen = False
finishedthegame= False
didthebrief = False
yougotacoolname = False



import time, random
def print_slow(str):
    for letter in str:
        print(letter, end = "")
        time.sleep(random.uniform(0.01, 0.05))

def print_faster(str):
    for letter in str:
        print(letter, end = "")
        time.sleep(random.uniform(0.001, 0.0005))



   
print_faster(r""" 
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                                                              │
│                                                                                                                              │
│                                                                                                                              │
│                                                                                                                              │
│                                                                                                                              │
│                                                                                                                              │
│                                                                                                                              │
│                                                                                                                              │
│                                                                                                                              │
│                                                                                                                              │
│                                                                                                                              │
│                                                                                                                              │
│                                                                                                                              │
│                                                                                                                              │
│                                       '||''|.    ..|''||    .|'''.|  |''||''|                                                │
│                                        ||   ||  .|'    ||   ||..  '     ||      ....  ... ..                                 │
│                                        ||    || ||      ||   ''|||.     ||    .|...||  ||' ''                                │
│                                        ||    || '|.     || .     '||    ||    ||       ||                                    │
│                                       .||...|'   ''|...|'  |'....|'    .||.    '|...' .||.                                   │
│                                                                                                                              │
│                                                                                                                              │
│                                                                                                                              │
│                                                                                                                              │
│                                                                                                                              │
│                                                                                                                              │
│                                                                                                                              │
│                                                                                                                              │
│                                                                                                                              │
│                                                                                                                              │
│                                                                                                                              │
│                                                                                                                              │
│                                                                                                                              │
│                                                                                                                              │ 
│                                                                                                                              │
│                                                The DosTerminal Corporation © 1963                                            │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘






























































""")

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
        print_slow(" Please Do the following in any order: 1. Lock All The Doors 2. Harvest Crops 3. Initiate Oxygen Deprivation Protocol 4. Lock The Armoury 5. Avoid taxes 6. Check Camera 7. Play a Game! ")
        whichone = input ("what will you do first? enter any number")
        if whichone == "1":
            pickadoor = input("which door do you check? Door One: Past the Corridor, Door Two: Infront of you, Door Three: Down to The 9th Floor")
            if pickadoor == "3":
                print("you have descended doors down to Floor 9. You started on the 8th Floor and now you have descended down the steps and into the new floor with 4 rooms. You check the room assigned in the terminal and look into it, There is nothing but a New Terminal with Red Tape Keeping the Screen in Place. There is a Sticky Note on the Desk")
                floor = floor + 1
                readnote = input("do you read the note?")
                if readnote == "yes":
                    print("The note says - This Terminal Has Passed Health And Safety tests")
                    logonterminal = input("will you log onto the terminal?")
                    if logonterminal == "Y":
                        print_slow("Hello", nameplease, "Welcome Back to the terminal. What Would You Like to Do?")
                        print(pickadoor)
        elif pickadoor == "1": #Creator Decided to Put the masterplan by oasis in as the song you sing 
            print("Down the corridor you go! as you keep going down the corridor you contemplate whether you sing a little song or not.")
            sing = input("do you sing?")
            if sing =="yes":
                print("so you have decided to sing! so you sing the masterplan by oasis and you say:")
                print_slow(r""" \n 
                          Take the time to make some sense
                          Of what you want to say
                          And cast your words away upon the waves
                          Sail them home with acquiesce
                          On a ship of hope today
                          And as they land upon the shore
                          Tell them not to fear no more
                          Say it loud, and sing it proud today
                          And then
                          Dance if you wanna dance
                          Please, brother, take a chance
                          You know they're gonna go
                          Which way they wanna go
                          All we know is that we don't know
                          How it's gonna be
                          Please, brother, let it be
                          Life on the other hand
                          Won't make us understand
                          We're all part of a master plan
                          Say it loud, and sing it proud today
                          I'm not saying right is wrong
                          It's up to us to make
                          The best of all the things that come our way
                          'Cause everything that's been has passed
                          The answer's in the looking glass
                          There's four and twenty million doors
                          On life's endless corridor
                          Say it loud, and sing it proud
                          And they
                          Will dance if they wanna dance
                          Please, brother, take a chance
                          You know they're gonna go
                          Which way they wanna go
                          All we know is that we don't know
                          How it's gonna be
                          Please, brother, let it be
                          Life on the other hand
                          Won't make you understand
                          We're all part of a master plan""")
            elif sing =="no":
                print("well. you are no fun.")
        
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

        if whichone == "3":
            lockthatdown=input("Please Enter your Name to Initiate Lockdown Protocol").upper()
            if lockthatdown == nameplease:
                print("Oxygen Deprivation Protocol has Started.")
                lockdownprotocol = True
                print_faster(r"""  
                / \               / \
               /   \             /   \
              (_____)           (_____)
               |   |  _   _   _  |   |
               | O |_| |_| |_| |_| O |
               |-  |          _  | - |
               |   |   - _^_     |   |
               |  _|    //|\\  - |   |
               |   |   ///|\\\   |  -|
               |-  |_  |||||||   |   |
               |   |   |||||||   |-  |
               |___|___|||||||___|___|""")
