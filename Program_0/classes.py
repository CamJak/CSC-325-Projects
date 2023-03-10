from random import randint

# Simple node class
class node:
    def __init__(self, data) -> None:
        self.data = data
        self.link = None

    # Acessors
    @property
    def data(self):
        return self._data

    @property
    def link(self):
        return self._link
    
    # Mutators
    @data.setter
    def data(self, data):
        self._data = data

    @link.setter
    def link(self, link):
        self._link = link


# Linked list class
class linkedList:
    def __init__(self, num_nodes) -> None:
        self.length = num_nodes
        self.head = node(randint(0,100))
        self.prev = self.head

        # Generate linked list
        # Data is a random number from 0 to 100
        for i in range(num_nodes-1):
            newNode = node(randint(0,100))
            self.prev.link = newNode
            self.prev = newNode

        self.tail = self.prev

    # Returns string version of linked list
    def __str__(self) -> str:
        str_out = ""
        currNode = self.head
        for i in range(self.length):
            str_out = str_out + str(currNode.data) + " "
            currNode = currNode.link
        return str_out
    
    # Function to return first node containing matching data
    def find(self, currNode, data) -> node:
        while (currNode.data != data):
            currNode = currNode.link
        return currNode

    # Function to sort linked list using selection sort
    # Checks each node against all nodes to its right and swaps with minimum data node
    def sort(self) -> None:
        index = 1
        currNode = self.head
        while (index < self.length):
            minData = currNode.data
            peekNode = currNode.link
            while (peekNode != None):
                minData = min(peekNode.data, minData)
                peekNode = peekNode.link
            self.find(currNode, minData).data = currNode.data
            currNode.data = minData
            currNode = currNode.link
            index += 1
