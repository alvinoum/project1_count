# Ask for user's name and display is back
# Ask user for a number input n, then count from 0 to n on the screen
# Learn and use the best practice coding standards and conventions
# Modify the program to count by 2s or some other incrment
# Sanitize all input and test to verify!
# And error-checking and graceful error handling
# Naming conventions are all in lowercase due to multiple programs
# Do not name the folder the same as the program...
# Save as new versions and consider a changelog

person = input ('Enter your name: ')
print ('Hello ', person)

# Alphabet p
while True:
    try:
        input = int(person('Enter your name using only the Alphabet. '))
        # Check if input uses only Alphabet
        if input in range (a,z):
            break
        else:
            print ('Please use only the Alphabet.')
    except:
        print ('That is not in the Alphabet!')

# filter only letters in input
def person(input):
    valids = []
    for character in input:
        if character in letters:
            valid.append( character)
    return (valids)
        


        
        
        
a = 0
b = 1
count = 0
#maxNum = 100

print ('Enter numbers to count by.')
print ('Enter 0 to quit.')

#converted string to integer
maxNum = int(input('Please enter a number over 0: '))

#Need to add validation and sani
#Nothing lower then 0




#while count < max_count:
#    count = count +





#while a != 0:
#  while s < 100:
#   print ('Count by:', s) 
#    s = a + s
#    print (a)

for i in range(0, maxNum, 2):
    print(i)