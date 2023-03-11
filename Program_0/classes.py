## File to hold the Node and LinkedList classes

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
    # Initialize linked list with head data
    def __init__(self, headData) -> None:
        self.length = 1
        self.head = node(headData)
        self.tail = self.head

    # Returns string version of linked list
    def __str__(self) -> str:
        str_out = ""
        currNode = self.head
        for i in range(self.length):
            str_out = str_out + str(currNode.data) + " "
            currNode = currNode.link
        return str_out
    
    # Function to append new nodes
    def append(self, data) -> None:
        newNode = node(data)
        self.tail.link = newNode
        self.tail = newNode
        self.length += 1
    
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
