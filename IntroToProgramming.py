total = 0
life = 1
import time, random
def print_slow(str):
    for letter in str:
        print(letter, end = "")
        time.sleep(random.uniform(0.1, 0.05))

def print_faster(str):
    for letter in str:
        print(letter, end = "")
        time.sleep(random.uniform(0.01, 0.005))



while life == 1:
    print_faster(r""" 
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│                                                                 │
│                                                                 │
│                                                                 │
│                                                                 │
│     '||''|.    ..|''||    .|'''.|  |''||''|                     │
│      ||   ||  .|'    ||   ||..  '     ||      ....  ... ..      │
│      ||    || ||      ||   ''|||.     ||    .|...||  ||' ''     │
│      ||    || '|.     || .     '||    ||    ||       ||         │
│     .||...|'   ''|...|'  |'....|'    .||.    '|...' .||.        │
│                                                                 │
│                                                                 │
│                                                                 │
│                                                                 │
│                  The DosTerminal Corporation                    │
└─────────────────────────────────────────────────────────────────┘
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
    if life == 1:
        print_slow("Please Do the following in any order: 1. Lock All The Doors 2. Harvest Crops 3. Initiate Oxygen Deprivation Protocol 4. Lock The Armoury 5. Avoid taxes")