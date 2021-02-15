class arrayADT():

    def __init__(self):
        pass

    # INSERT(x,p,L)
    def insert(self, insert, position, list_input):
        self.list_input = list_input
        self.insert = insert
        self.position = position
        # Check if position is outside of list length
        if(self.position <= len(self.list_input) and self.position >= 0):
            # save values in array after position to temp_list
            temp_list = self.list_input[self.position:]
            self.list_input = self.list_input[:self.position]
            # append the new value to the end of the list
            self.list_input.append(self.insert)
            # add the test list back on after our new value
            self.list_input.extend(temp_list)
            print(f"{self.list_input}")
        else:
            print("Undefined")

    # LOCATE(x, L)
    def locate(self, key, list_input):
        self.list_input = list_input
        self.key = key
        endLflag=0
        # find index and print the corresponding value
        for i in range(len(self.list_input)):
            if self.list_input[i] == self.key:
                print(f"{i}")
                endLflag=1
        if(endLflag!=1): 
                print("END(L)")

    # RETRIEVE(p, L)
    def retrieve(self, position, list_input):
        self.list_input = list_input
        self.position = position
        if(self.position <= len(self.list_input) and self.position >= 0):
            # print value of the array at specified index
            print(f"{self.list_input[self.position]}")
        else:
            print("undefined")

    # DELETE(p, L)
    def delete(self, position, list_input):
        self.list_input = list_input
        self.position = position
        if(self.position <= len(self.list_input) and self.position >= 0):
            self.list_input.pop(self.position)
            print(f"{self.list_input}")
        else:
            print("undefined")

    # NEXT(p, L)
    def next_(self, position, list_input):
        self.list_input = list_input
        self.position = position
        if(self.position == len(self.list_input)+1):
            print("END(L)")
        elif(self.position == len(self.list_input)+2):
            print("Undefined")
        else:
            print(f"{self.list_input[self.position+1]}")    

    # PREVIOUS(p, L)
    def previous(self, position, list_input):
        self.list_input = list_input
        self.position = position
        if(self.position == 0):
            print("Undefined")
        else:
            print(f"{self.list_input[self.position-1]}")

    # MAKENULL(L)
    # Need to add END(L) functionality 
    def makeNull(self, list_input):
        self.list_input = list_input
        self.list_input = None
        print(f"END(L)")

    # FIRST(L)
    def first(self, list_input):
        self.list_input = list_input
        if(self.list_input == None):
            print("END(L)")
        else:
            print(f"{self.list_input[0]}")

    # PRINTLIST(L)
    def printList(self, list_input):
        self.list_input = list_input
        for i in range(len(self.list_input)):
            print(f"{self.list_input[i]}", end=" ")
        print("\n")


testArray = [1,2,3,4,5,6,7,8,9]
testArray2 = None

# insert test
# arrayADT().insert(100, 1, testArray)

# locate test
# arrayADT().locate(100, testArray)

# retrieve test
# arrayADT().retrieve(2, testArray)

# delete test
# arrayADT().delete(1, testArray)

# next test
# arrayADT().next_(11, testArray)

# previous test
# arrayADT().previous(0, testArray)

# makeNull test
# arrayADT().makeNull(testArray)

# first test
# arrayADT().first(testArray2)

# printList test
# arrayADT().first(testArray)