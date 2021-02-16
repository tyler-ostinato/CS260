from timeit import default_timer as timer 

class linkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

class linkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value, position, input_list):
        self.position = position
        self.input_list = input_list
        node = linkedListNode(value)
        if self.head == None: #Put this for all??????? Maybe not actually
            self.head = node
            return
        currentNode = self.head
        if self.position == 0:
            tempVal = currentNode.value
            currentNode.value = value
            ll.insert(tempVal,1,self.input_list)
            return
        for i in range(self.position-1):
            if currentNode.nextNode is None: #If we reach end of list
                if self.position-2 == i: # are we trying to insert at end?
                    break 
                return "UNDEFINED"
            currentNode = currentNode.nextNode

        tempNode = currentNode.nextNode
        currentNode.nextNode = node
        currentNode = currentNode.nextNode #after get
        currentNode.nextNode = tempNode

    def delete(self, position, input_list):
        self.position = position
        self.input_list = input_list
        currentNode = self.head
        #Do I need the self.head stuff? No I think
        if currentNode is None:
            return "UNDEFINED"
        if self.position == 0:
            tempNode = currentNode.nextNode
            if tempNode is None:
                return "UNDEFINED"
            tempVal = tempNode.value
            ll.delete(1,self.input_list)
            currentNode.value = tempVal
            return
        for _ in range(self.position-1):
            if currentNode.nextNode is None:
                return "UNDEFINED"
            currentNode = currentNode.nextNode
        tempNode = currentNode.nextNode
        if tempNode is None:
            return "UNDEFINED"
        tempNode = tempNode.nextNode
        currentNode.nextNode = tempNode
                    

    def makenull(self, input_list):
        self.input_list = input_list
        # currentNode = self.head
        # currentNode.nextNode = None
        self.head = None

    def first(self, input_list):
        if self.head == None:
            return "UNDEFINED"
        return 0
    
    def end(self, input_list):
        self.input_list = input_list
        self.position = 0
        if self.head == None:
            return "UNDEFINED"
        currentNode = self.head #need to test if list is empty. For all???
        while True:
            if currentNode.nextNode is None:
                self.position += 1
                return self.position
            currentNode = currentNode.nextNode
            self.position += 1

    def locate(self, value, input_list):
        self.input_list = input_list
        self.position = 0
        currentNode = self.head #need to test if list is empty. For all???
        while True:
            if currentNode.value == value:
                return self.position
            elif currentNode.nextNode is None:
                return ll.end(self.input_list)
            
            currentNode = currentNode.nextNode
            self.position += 1
            # print(currentNode)

    def retrieve(self, position, input_list):
        self.position = position
        self.input_list = input_list
        currentNode = self.head
        for _ in range(self.position):
            if currentNode.nextNode is None:
                return "UNDEFINED"
            currentNode = currentNode.nextNode
        return currentNode.value

        # currentNode.nextNode = node


        # currentNode = self.head
        # for i in range(self.position):
        #     targetNode = currentNode.nextNode
        #     print(targetNode.value)

        # currentNode = self.head
        # while True:
        #     if currentNode.nextNode is None:
        #         currentNode.nextNode = node
        #         break
        #     currentNode = currentNode.nextNode
        
    def next(self, position, input_list):
        self.position = position
        tempPosition = 0
        self.input_list = input_list 
        currentNode = self.head
        for _ in range(self.position+1):
            if currentNode.nextNode is None:
                if tempPosition != self.position:
                    return "UNDEFINED"
                else:
                    return ll.end(self.input_list)
            currentNode = currentNode.nextNode
            tempPosition+=1
        self.position = tempPosition
        return self.position

    def previous(self, position, input_list):
        self.position = position
        tempPosition = 0
        self.input_list = input_list 
        currentNode = self.head
        if self.position == 0:
            return "UNDEFINED"
        for _ in range(self.position-1):
            if currentNode.nextNode is None:
                if tempPosition != self.position:
                    return "UNDEFINED"
                else:
                    return ll.end(self.input_list)
            currentNode = currentNode.nextNode
            tempPosition+=1
        self.position = tempPosition
        return self.position
        
        
        





    def printLinkedList(self, input_list):
        self.input_list = input_list
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value, "-> ", end="")
            currentNode = currentNode.nextNode
        print("None")


ll = linkedList()
# random.seed(1)
pointer_list = None

pointer_list = ll.insert(23,0,pointer_list)

# insert test
pointer_list = ll.insert(4, 1, pointer_list)
# ll.printLinkedList(pointer_list)
pointer_list = ll.insert(10, 2, pointer_list)
# ll.printLinkedList(pointer_list)
pointer_list = ll.insert(23, 3, pointer_list)
# ll.printLinkedList(pointer_list)
pointer_list = ll.insert(253, 4, pointer_list)
# ll.printLinkedList(pointer_list)
pointer_list = ll.insert(536, 5, pointer_list)
# ll.printLinkedList(pointer_list)
pointer_list = ll.insert(78, 6, pointer_list)
# ll.printLinkedList(pointer_list)
pointer_list = ll.insert(456, 7, pointer_list)
# ll.printLinkedList(pointer_list)
pointer_list = ll.insert(475, 20, pointer_list)
pointer_list = ll.insert(475, 8, pointer_list)
pointer_list = ll.insert(475, 69, pointer_list)
print("This is the pointer list: ",end = " ")
ll.printLinkedList(pointer_list)


print("This is list after insert at beginning: ", end=" ")
pointer_list = ll.insert(35, 0, pointer_list) 


# printList test
ll.printLinkedList(pointer_list)

pointer_list = ll.delete(0,pointer_list) 
print("First element deleted:",end=" ")
ll.printLinkedList(pointer_list)


print("This is first:",ll.first(pointer_list))
print("This is end:",ll.end(pointer_list))
print("This is locate:",ll.locate(69,pointer_list))
print("This is retrieve:",ll.retrieve(0,pointer_list))
print("This is next:",ll.next(8,pointer_list))
print("This is previous:",ll.previous(3,pointer_list))
ll.makenull(pointer_list)
print("This is the list after makenull: ", end = " ")
ll.printLinkedList(pointer_list)
