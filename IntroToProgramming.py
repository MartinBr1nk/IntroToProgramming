total = 0
life = 1
floor = 8
cropamount = 0


import time, random
def print_slow(str):
    for letter in str:
        print(letter, end = "")
        time.sleep(random.uniform(0.1, 0.05))

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

print("Terminal Buddy - Jan 24th 1963")
nameplease= input("Input Agent Name ")
print("Hello", nameplease, "You have been granted the highest level of authorisation  ") 
incomingmessage = input("incoming message from UNKNOWN - Origin HOMEBASE, REDACTED. Accept? Y/N")
if incomingmessage == "Y":
        print_slow("Connection Secured. This is Captain REDACTED. We regret to inform you that your base has been comprimised. Please follow the measures in the next transmission. CONNECTION TERMINATED")
elif incomingmessage == "N":
        print("You hear a noise coming from above you. Curious you leave the secure room and investigate, An Intruder then with a machete beheads you and it is game over.")
        life = 0
while life == 1:       
        print_slow("Please Do the following in any order: 1. Lock All The Doors 2. Harvest Crops 3. Initiate Oxygen Deprivation Protocol 4. Lock The Armoury 5. Avoid taxes 6. Check Camera 7. Play a Game!")
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
        if whichone == "2":
            print("you go to the open space which has lights on 24/7 to simulate daytime, there are different crops available to harvest: Corn, Potatoes, Carrot, Lettuce, Cabbage, Tomatoes, Pumpkins, Watermelon, Onions and Strawberries ")
            harvestmoon = input("what would you like to harvest? (0 to end) ")
            while harvestmoon != "0":
                print("you have succesfully harvested a crop")
