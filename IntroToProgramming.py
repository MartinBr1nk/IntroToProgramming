total = 0
import time, random
def print_slow(str):
    for letter in str:
        print(letter, end = "")
        time.sleep(random.uniform(0.1))


print("Terminal Buddy - Jan 24th 1963")
nameplease= input("Input Agent Name ")
print("Hello", nameplease, "You have been granted the highest level of authorisation  ") 
incomingmessage = input("incoming message from UNKNOWN - Origin HOMEBASE, REDACTED. Accept?")
if incomingmessage == "YES":
    print_slow("Connection Secured. This is Captain REDACTED. We regret to inform you that your base has been comprimised. Please follow the measures in the next transmission. CONNECTION TERMINATED")