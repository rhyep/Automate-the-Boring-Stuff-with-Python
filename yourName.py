#name=''

#>WHILE LOOP<

#while name != 'your name': 
#    print('Please type your name:')
#    name=input()
#print('Thank you!')

# >BREAK statement<

#while True: 
#    print('Please type your name:')
#    name=input()
#    if name == 'your name':
#        break
#print('Thank you!')

# >CONTINUE statement<

spam = 0
while spam <5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))
