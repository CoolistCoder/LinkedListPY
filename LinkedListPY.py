"""
Python project for defining and implementing a basic linked list
"""

class node:
    next = None         #The node next to the current node
    data = 0            #The data stored within the current node

class linkedlist:
    head = None       #the first node in the linked list
    
    def insert(self, data): #inserts data into the linked list
        if self.head == None:                #if the head is empty...     
            self.head = node()               #make the empty head a new node
            self.head.data = data;           #set the data of this new head to the data we need
        else:
            temp = self.head                 #the head must be iterated if it isn't empty
            while temp.next != None:    #go through using our iterator until we hit the end
                temp = temp.next
            temp.next = node()               #once at the end, we need to give the position we're at a new node
            temp.next.data = data            #and give that new node data

    def print(self): #prints out each element of the linked list
        if self.head == None:           #if the head is empty...
            print("The list is empty!") #just let us know
        else:                           #if the head is not empty...
            temp = self.head            #make a temporary node as a form of traversal
            while temp != None:         #iterate until the node we're at is null
                print(temp.data)        #print the data out at the node we're at
                temp = temp.next        #go to the next node

    def len(self):   #retrieves the length of the linked list
        if self.head == None:           #if the head is empty...
            print("The list is empty!") #let us know
            return 0                    #return 0 as a way to indicate there are no elements in the list
        else:                           
            counter = 0                 #create a simple counter
            temp = self.head            #make a temporary node as a form of traversal
            while temp != None:         #iterate until the node we're at is null
                counter = counter + 1   #count up for every non null we've found
                temp = temp.next        #go to the next node
            return counter              #return the number of nodes we counted!
                
    def get(self, at): #returns data at a specific position
        if self.head == None:                   #If the head is empty...
            return "Empty list"                 #return "empty list" if the head is not populated with data
        else:                                   #if the head has data...
            if at < self.len() and at >= 0:     #need to determine if we're out of range
                counter = 0                     #if at is not out of range, create a counter to iterate
                temp = self.head                #populate the head node as well
                while (counter < at):           #while our counter is counting up to at, iterate through nodes
                    counter = counter + 1
                    temp = temp.next
                return temp.data                #once we reach where we need to, return the data at the node
            else:
                return "Out of range"           #return out of range if our at is larger than our length
            
                
            



#create our new linked list and populate it with data
new_list = linkedlist()
new_list.insert(32)
new_list.insert(25)
new_list.insert(38)
new_list.insert(102)
new_list.insert(8)
new_list.print()

get_at = 3  #this value is used to retrieve the element at the position we want
print("The data at " + str(get_at) + " is: " + str(new_list.get(get_at)))   #retrieve data at get_at
get_at = 0
print("The data at " + str(get_at) + " is: " + str(new_list.get(get_at)))   #retrieve data at get_at
get_at = 45
print("The data at " + str(get_at) + " is: " + str(new_list.get(get_at)))   #retrieve data at get_at