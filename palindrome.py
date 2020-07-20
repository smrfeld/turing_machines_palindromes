import string
import sys
from turing import Turing_Machine

def check_palindrome(initial_string):
        
    # Define Character Set (allowed characters for the palindrome)
    character_list = list(string.ascii_lowercase)
    character_list.append(' ') # to allow for spaces

    # Initial string
    print('Checking: ' + initial_string)
    print('- - -')
    initial_list = list(initial_string)

    # Quick check that you only used allow characters
    for i in initial_list:
        if i not in character_list:
            print('Error! Initial character >',i,'< not in allowed character list!')
            sys.exit()

    # Append list
    initial_list.append(0)

    # Set up the turing machine
    i_write_head = 0
    i_state = 'q1' # initial state
    i_tape_list = initial_list

    # Initiate the class
    runMachine = Turing_Machine(i_state,i_write_head,i_tape_list)
    print(runMachine.getState(),runMachine.getHead(),runMachine.getList())

    # Run the machine
    ctr=0
    while runMachine.getState() != 'qy' and runMachine.getState() != 'qn' and ctr < 1000:
        runMachine.updateMachine(character_list)
        print(runMachine.getState(),runMachine.getHead(),runMachine.getList())
        ctr += 1
    print('- - -')

    # Printout result
    if (runMachine.getState() == 'qy'):
        print(initial_string,'is a palindrome! Steps:',ctr)
    else:
        print(initial_string,'is NOT a palindrome! Steps:',ctr)