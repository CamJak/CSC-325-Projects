from random import randint

class linkedList:
    def __init__(self, num_nodes) -> None:
        self.listNodes = []
        link = 0
        for x in range(num_nodes-1):
            newNode = node(randint(0,100), link)
            self.listNodes.append()

class node:
    def __init__(self, data, link) -> None:
        self.data = data
        self.link = link
