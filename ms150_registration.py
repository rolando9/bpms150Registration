# 02/09/2018
# Rolando Paz
# This program will create a dictionary of all BPMS150 entrants for the 2019 race

# Create empty dictionary

racer_registrations = {}

# Set a flag to indicate that application process is open

reg_process = True

while reg_process:
    # Prompt applicant to provide name, address, type of bike
    name = input('What is the name of the registrant? ')
    bike = input('What kind of bike do you have? ')

    # Store the information in a dictionary
    racer_registrations[name] = bike

    # ask if the applicant has anyone else to enter
    repeat = input('Do you have anyone else to register? [yes/no] ')
    if repeat == 'no':
        reg_process = False

    # registration process is complete

print('\n--- BPMS 150 Registration Complete ---')
for name, bike in racer_registrations.items():
    print(name.title() + ' has registered for the 2019 BPMS 150 with a ' +
          bike.title() + '.')


