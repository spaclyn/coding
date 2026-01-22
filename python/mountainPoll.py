responses = {}

#set flag to indicate that the polling is active
pollingActive = True

while pollingActive:
    #prompt for the person's name and response
    name = input("\nWhat is your Name? ")
    response = input("Which mountain would you like to climb someday? ")

    #stores the response in the dictionary
    responses[name] = response

    #Find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (yes / no) ")
    if repeat == 'no':
        pollingActive = False
    
    #Polling is complete. Show the results
    print("\n --- Poll Results --- ")
    for name, response in responses.items():
        print(f"{name} would like to climb {response}.")

        
