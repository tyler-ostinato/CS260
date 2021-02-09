class arrayADT():
    
    def __init__(self):
        pass

    # INSERT(x,p,L)
    # Need to add undefined functionality
    def insert(self, insert, position, list_input):
        self.list_input = list_input
        self.insert = insert
        self.position = position
        # save values in array after position to temp_list
        temp_list = self.list_input[self.position:]
        self.list_input = self.list_input[:self.position]
        # append the new value to the end of the list
        self.list_input.append(self.insert)
        # add the test list back on after our new value
        self.list_input.extend(temp_list)
        print(f"{self.list_input}")

    # LOCATE(x, L)
    # Need to add undefined functionality
    def locate(self, key, list_input):
        self.list_input = list_input
        self.key = key
        # find index and print the corresponding value
        for i in range(len(self.list_input)):
            if self.list_input[i] == self.key:
                print(f"{i}")

    # RETRIEVE(p, L)
    # Need to add END(L) functionality
    def retrieve(self, position, list_input):
        self.list_input = list_input
        self.position = position
        # print value of the array at specified index
        print(f"{self.list_input[self.position]}")

    # DELETE(p, L)
    # Can we make this method this easy?
    # Need to add END(L) functionality
    def delete(self, position, list_input):
        self.list_input = list_input
        self.position = position
        self.list_input.pop(self.position)
        print(f"{self.list_input}")

    # NEXT(p, L)
    # Need to add undefined functionality
    def nextt(self, position, list_input):
        self.list_input = list_input
        self.position = position
        print(f"{self.list_input[self.position+1]}")

    # PREVIOUS(p, L)
    # Need to add undefined functionality
    def previous(self, position, list_input):
        self.list_input = list_input
        self.position = position
        print(f"{self.list_input[self.position-1]}")

    # MAKENULL(L)
    # Need to add END(L) functionality 
    def makeNull(self, list_input):
        self.list_input = list_input
        self.list_input = None
        print(f"{self.list_input}")

    # FIRST(L)
    # Need to add END(L) functionality 
    def first(self, list_input):
        self.list_input = list_input
        print(f"{self.list_input[0]}")

    # PRINTLIST(L)
    def first(self, list_input):
        self.list_input = list_input
        for i in range(len(self.list_input)):
            print(f"{self.list_input[i]}", end=" ")
        print("\n")


testArray = [3,1,1,1,5,1,1,1]

# insert test
# arrayADT().insert(5, 3, testArray)

# locate test
# arrayADT().locate(5, testArray)

# retrieve test
# arrayADT().retrieve(4, testArray)

# delete test
# arrayADT().delete(4, testArray)

# next test
# arrayADT().nextt(3, testArray)

# previous test
# arrayADT().previous(5, testArray)

# makeNull test
# arrayADT().makeNull(testArray)

# first test
# arrayADT().first(testArray)

# printList test
arrayADT().first(testArray)