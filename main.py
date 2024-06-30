print()  # any mistake will need the code to be restarted
print('''
====To check voter\'s eligibility in the following countries as of 2014:====''')
list = ["SINGAPORE", "NIGERIA", "AUSTRIA", "NORTH KOREA", "ENGLAND", "SAUDI ARABIA"]
for item in list:
    print('===', item)
print()
# Set a condition to determine when to stop looping
valid_response = False

# Use a while loop to repeat a block of code until a valid response is provided
while not valid_response:
    Thank = input('Are you from any of these countries, Yes or No: ')
    if Thank.upper() == 'YES' or Thank.upper() == 'Y':
        valid_response = True
        print()
        break
    elif Thank.upper() == 'NO' or Thank.upper() == 'N':
        valid_response = True
        print('Thank you but this isn\'t meant for you 👍')
        exit()
    else:
        print("Invalid response. Please try again.")
        print("Please check your spelling.")
        print()

# Continue with the rest of your code after a valid response is provided

valid_responser = False
while not valid_responser:
    Location = input('Which Country do you reside in? ')
    if Location.upper() in list:
        valid_responser = True
        break
    else:
        print("Invalid response. Please try again.")
        print("Please check your spelling.")
        print()

print()
if Location.upper() == 'ENGLAND':
    print('System is Mornachical, so voting doesn\'t take place and Prime Minister is chosen by appointment')
    exit()
elif Location.upper() == 'NORTH KOREA':
    print('System is Dictatorial. \nVoting takes place but doesn\'t really count. ')
    exit()

valid_responsetwo = False
while not valid_responsetwo:
    Gender = input('Are you a Male(M) or Female(F): ')
    if Gender.upper() == 'MALE' or Gender.upper() == 'M':
        valid_responsetwo = True
        Address = 'Mr'
    if Gender.upper() == 'FEMALE' or Gender.upper() == 'F':
        valid_responsetwo = True
        Address = 'Mrs'
    else:
        print("Invalid response. Please try again.")
        print("Please check your spelling.")
        print()

if Location.upper() == 'SAUDI ARABIA' and Address == 'Mrs':
    print()
    print('You are a WOMAN so your not allowed to vote. Sorry')
    exit()

Name = input('Please use your REAL name? ')  # Real function
Age = int(input('How old are you? '))

print()
if Location.upper() == 'SINGAPORE' and Age > 20:
    print(Address + ' ' + Name + ' is legally eligible to vote')
elif Location.upper() == 'SINGAPORE' and Age < 21:
    print(Address + ' ' + Name + ' is not eligible to vote. ')
    print(Address + ' ' + Name + ' is not of voting age, 21.')
    exit()

if Location.upper() == 'NIGERIA' and Age > 17:
    print(Address + ' ' + Name + ' is legally eligible to vote')
elif Location.upper() == 'NIGERIA' and Age < 18:
    print(Address + ' ' + Name + ' is not eligible to vote. ')
    print(Address + ' ' + Name + ' is not of voting age, 18.')
    exit()

if Location.upper() == 'AUSTRIA' and Age > 15:
    print(Address + ' ' + Name + ' is legally eligible to vote')
elif Location.upper() == 'AUSTRIA' and Age < 16:
    print(Address + ' ' + Name + ' is not eligible to vote. ')
    print(Address + ' ' + Name + ' is not of voting age, 16.')
    exit()

if Location.upper() == 'SAUDI ARABIA' and Age > 20 and Address == 'Mr':
    print(Address + ' ' + Name + ' is legally eligible to vote. ')
elif Location.upper() == 'SAUDI ARABIA' and Age < 21 and Address == 'Mr':
    print(Address + ' ' + Name + ' is  not eligible to vote. ')
    print(Address + ' ' + Name + ' is not of voting age, 21.')
    exit()
