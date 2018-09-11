birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'} #Dictionary stores the data

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '': #if name is blank then program will quit
        break

    if name in birthdays: #if name is in the Dictionary then print
        print(birthdays[name] + ' is the birthday of ' + name)

    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated!.')
