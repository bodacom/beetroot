
# General loop for the 'O' letter
for i in range(0,2):

    # loop for top and bottom lines
    for a in range(0,9):

        #printing the top and bottom lines
        print('#', sep='', end='')
        
    # printing the end of the bottom line
    print()

    # Checking whether new side lines are needed.
    # If were printed already than breaking the loop
    if i == 1:
        break
    # printing side lines    
    for b in range(0,3):
        print('#\t#')

# General loop for the 'H' letter
for i in range(0,2):

    # printing the end of the bottom line and separator of the letters
    print()
    
    # printing side lines    
    for b in range(0,2):
        print('#\t#')

    # Checking whether center line is needed.
    # If have printed one already than breaking the loop
    if i == 1:
        break
    
    # loop for center line
    for a in range(0,9):

        #printing the center line
        print('#', sep='', end='')
