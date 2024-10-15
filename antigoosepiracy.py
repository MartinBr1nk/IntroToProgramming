import os
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
            time.sleep(5)
            print("\n")
    elif gcheck == True:
        print("Goose Detected. Launcing Software")

    #If the goose is NOT present then the program WILL NOT WORK.
    #DO NOT REMOVE THIS CODE. THE PROGRAM WILL NOT WORK WITHOUT IT.
goose_check()