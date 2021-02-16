from timeit import default_timer as timer 

class arrayADT():

    def __init__(self):
        pass

    # INSERT(x,p,L)
    def insert(self, value, position, list_input):
        self.list_input = list_input
        self.value = value
        self.position = position
        # Check if position is outside of list length
        if(self.position <= len(self.list_input) and self.position >= 0):
            # save values in array after position to temp_list
            temp_list = self.list_input[self.position:]
            self.list_input = self.list_input[:self.position]
            # append the new value to the end of the list
            self.list_input.append(self.value)
            # add the test list back on after our new value
            self.list_input.extend(temp_list)
            return self.list_input
        else:
            return "UNDEFINED"

    # LOCATE(x, L)
    def locate(self, value, list_input):
        self.list_input = list_input
        self.value = value
        endLflag=0
        # find index and print the corresponding value
        for i in range(len(self.list_input)):
            if self.list_input[i] == self.value:
                endLflag=1
                return i
        if(endLflag!=1): 
                return arrayADT().end(self.list_input)

    # RETRIEVE(p, L)
    def retrieve(self, position, list_input):
        self.list_input = list_input
        self.position = position
        if(self.position <= len(self.list_input) and self.position >= 0):
            # print value of the array at specified index
            return self.list_input[self.position]
        else:
            return "UNDEFINED"

    # DELETE(p, L)
    def delete(self, position, list_input):
        self.list_input = list_input
        self.position = position
        if(self.position <= len(self.list_input) and self.position >= 0):
            self.list_input.pop(self.position)
            return self.list_input
        else:
            return "UNDEFINED"

    # NEXT(p, L)
    def next_(self, position, list_input):
        self.list_input = list_input
        self.position = position
        if len(self.list_input) >= self.position:
            return (self.position+1)
        else:
            return "UNDEFINED"


    # PREVIOUS(p, L)
    def previous(self, position, list_input):
        self.list_input = list_input
        self.position = position
        if(self.position == 0):
            return "UNDEFINED"
        else:
            return (self.position+1)

    # MAKENULL(L)
    # Need to add END(L) functionality 
    def makeNull(self, list_input):
        self.list_input = list_input
        self.list_input = []
        return  self.list_input

    # FIRST(L)
    def first(self, list_input):
        self.list_input = list_input
        if self.list_input is None:
            return "UNDEFINED"
        if len(self.list_input) == 0:
            return "UNDEFINED"
        else:
            return 0
    
    def end(self, list_input):
        self.list_input = list_input
        if self.list_input is None:
            return "UNDEFINED"
        if len(self.list_input) == 0:
            return "UNDEFINED"
        else:
            return len(self.list_input)+1


    # PRINTLIST(L)
    def printList(self, list_input):
        self.list_input = list_input
        for i in range(len(self.list_input)):
            print(f"{self.list_input[i]}", end=" ")
        print("\n")


testArray = [1,2,3,4,5,6,7,8,9]


# insert test
arrayADT().insert(100, 1, testArray)

# locate test
print("This is locate:", arrayADT().locate(100, testArray))

# retrieve test
print("This is retrieve:",arrayADT().retrieve(2, testArray))

# delete test
arrayADT().delete(1, testArray)

# next test
print("This is next:",arrayADT().next_(11, testArray))

# previous test
print("This is previous:",arrayADT().previous(0, testArray))

# first test
print("This is first:",arrayADT().first(testArray))

print("This is printed list: ",end=" ")
# printList test
arrayADT().printList(testArray)

print("This is printed list after make null: ",end=" ")
# makeNull test
testArray = arrayADT().makeNull(testArray)
arrayADT().printList(testArray)



