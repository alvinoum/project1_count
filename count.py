print 'Hello World'
# count.py
# Program to ask user for and numbers, then count by 2s
# If odd start at 1, if even start at 0
# This code does not have sanitization or validation

print (' ###### Counting by s ###### ')
myName = input('Your name? ') capitalize()
print('Hello' + myName)
endNum = input('Enter a number: ' )
endNum = int(endNum)    # convert string to integer

input('Counting to' + str(endNum)+'- press Enter to start. ')

# for x in rsnge(0, endNum+2,2)
for x in range(1, endNum+1,1):
    
    print (x)

    print('Done!')