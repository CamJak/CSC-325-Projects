import sys

class Trie:
    def __init__(self):
        self.start = None

    class TrieNode:
        def __init__(self, item, next = None, follows = None):
            self.item = item
            self.next = next
            self.follows = follows

    def __insert(node, key):
        # check if we've reached the end of the key
        if len(key) == 0:
            return None
        # check if we've reached the end of the trie
        if node == None:
            return Trie.TrieNode(key[0], None, Trie.__insert(None, key[1:]))
        # check if the first unit of the key matches the current node
        if key[0] == node.item[0]:
            node.follows = Trie.__insert(node.follows, key[1:])
            return node
        
        node.next = Trie.__insert(node.next, key)
        return node
    
    def insert(self, key):
        self.start = Trie.__insert(self.start, key+"$")

    def __contains(node, key):
        # check if we've reached the end of the key
        if not len(key):
            return True
        # check if we've reached the end of the trie
        if node in [None]:
            return False
        # check if the first unit of the key matches the current node
        if key[0] in [node.item[0]]:
            return Trie.__contains(node.follows, key[1:])

        # otherwise, check the next node
        return Trie.__contains(node.next, key)
    
    def __contains__(self, key):
        return Trie.__contains(self.start, key+"$")

    # print the trie
    def __str(node, indent):
        if node == None:
            return ""

        return f"\n{indent}{str(node.item)}{Trie.__str(node.follows, indent + ' ')}{Trie.__str(node.next, indent)}"

    def __str__(self):
        return Trie.__str(self.start, "")

def main():
    words = open(sys.argv[1], "r")    
    trie = Trie()
    # iterate through each word in the dictionary file and add it to the trie
    for line in words:
        word = line.strip()
        trie.insert(word)
        
    print("Misspelled words:")

    # open given text file and iterate through each word
    text = open(sys.argv[2], "r")
    for line in text:
        for word in line.split():
            word = word.lower().strip(',').strip('.')

            # check if word is in our dictionary and if not, print it
            if word not in trie:
                print(f"\t{word}")
                        
main()
