class Turing_Machine:

    def __init__(self,state,write_head,tape_list):
        self.state = state
        self.write_head = write_head
        self.tape_list = tape_list

    def getState(self):
        return self.state

    def getHead(self):
        return self.write_head
    
    def getList(self):
        return self.tape_list

    # Table of rules!
    def updateMachine(self, character_list):

        # Initial State
        if (self.state == 'q1'):
            if (self.tape_list[self.write_head] != 0):
                ### STATE ### (p)
                char_read = self.tape_list[self.write_head]
                char_index = character_list.index(char_read)
                self.state = ''.join(['p',str(char_index)])
                ### WRITE ### (zero)
                self.tape_list[self.write_head] = 0
                ### MOVE ### (right)
                self.write_head += 1
            else:
                ### STATE ### (qy)
                self.state = 'qy'
                ### WRITE ### (zero, unchanged)
                self.tape_list[self.write_head] = 0
                ### MOVE ### (right) (doesnt matter)
                self.write_head += 1
    
        elif (self.state.startswith('p')):
            if (self.tape_list[self.write_head]!=0):
                ### STATE ### (unchanged)
                self.state = self.state
                ### WRITE ### (unchanged)
                self.tape_list[self.write_head] = self.tape_list[self.write_head]
                ### MOVE ### (right)
                self.write_head += 1
            else:
                ### STATE ### (r)
                self.state = ''.join(['r',self.state[1:]])
                ### WRITE ### (zero, unchanged)
                self.tape_list[self.write_head] = 0
                ### MOVE ### (left)
                self.write_head -= 1
                    
        elif (self.state.startswith('r')):
            char_read = character_list[int(self.state[1:])]
            if (self.tape_list[self.write_head] != char_read and self.tape_list[self.write_head] != 0): # zero is needed for strings of odd length
                ### STATE ### (qn)
                self.state = 'qn'
                ### WRITE ###
                self.tape_list[self.write_head] = self.tape_list[self.write_head]
                ### MOVE ### (left) (doesn't matter)
                self.write_head -= 1
            else:
                ### STATE ###
                self.state = 'q2'
                ### WRITE ### (zero)
                self.tape_list[self.write_head] = 0
                ### MOVE ### (left)
                self.write_head -= 1
                
        elif (self.state == 'q2'):
            if (self.tape_list[self.write_head] != 0):
                ### STATE ### (unchanged)
                self.state = 'q2'
                ### WRITE ### (unchanged)
                self.tape_list[self.write_head] = self.tape_list[self.write_head]
                ### MOVE ### (left)
                self.write_head -= 1
            else:
                ### STATE ### (q1)
                self.state = 'q1'
                ### WRITE ### (zero)
                self.tape_list[self.write_head] = 0
                ### MOVE ### (right)
                self.write_head += 1