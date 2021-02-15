import random

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
        if self.head == None:
            self.head = node
            return
        
        # currentNode = self.head
        # for i in range(self.position):
        #     targetNode = currentNode.nextNode
        #     print(targetNode.value)

        currentNode = self.head
        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break
            currentNode = currentNode.nextNode
        


    def locate(self, value, input_list):
        pass

    def printLinkedList(self, input_list):
        self.input_list = input_list
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value, "-> ", end="")
            currentNode = currentNode.nextNode
        print("None")


# Generate a random linked list to perform calculations on
ll = linkedList()
random.seed(1)
pointer_list = None
for i in range(15):
    pointer_list = ll.insert(random.randint(1,100), 2 ,pointer_list)


# insert test
ll.insert(4, 2, pointer_list)

# printList test
ll.printLinkedList(pointer_list)
