class HashSet:
    """A class to represent a set abstract data type."""   
    def __init__(self, contents=[]):
        """
        Constructs all the necessary attributes for the person object.
        Takes a list as a parameter & sets up items and numItems instance variables.
        """
        self.items = [None] * 10
        self.numItems = 0

        # adds items form a given list to a items instance variable 
        for item in contents:
            self.add(item)
    
    class __Placeholder:
        """
        A class to represent a Placeholder type.
        Used for removing items that are not at the end of a chain.
        """
        def __init__(self):
            pass

        def __eq__(self, other):
            return False
        
    def __add(item, items):
        """
        Helper function responsible for:
        - calculating an index (hashing and %);
        - performing linear probing (collision resolution).
        """       
        # modulo (%) is required to keep hashes within list size range
        idx = hash(item) % len(items)

        loc = -1

        # linear probing loop
        while items[idx] != None:
            if items[idx] == item:
                return False
            
            if (loc < 0) and (type(items[idx]) == HashSet.__Placeholder):
                loc = idx

            idx = (idx + 1) % len(items)

        if loc < 0:
            loc = idx
            
        items[loc] = item

        return True

    def __rehash(oldList, newList):
        """
        Helper function responsible for rehashing values.
        Used when list size is changed due to a load factor reaching threshold.
        """ 
        for x in oldList:
            if (x != None) and (type(x) != HashSet.__Placeholder):
                HashSet.__add(x, newList)
                
        return newList
    
    def __remove(item, items):
        """
        Helper function responsible for removing items from a chain.
        """       
        idx = hash(item) % len(items)

        # loop to go through the items in the chain starting at hashed index
        while items[idx] != None:
            if items[idx] == item:
                nextIdx = (idx + 1) % len(items)
                # substitute item with None if at the end of a chain
                if items[nextIdx] == None:
                    items[idx] = None
                # substitute item with Placeholder if not at the end of a chain
                else:
                    items[idx] = HashSet.__Placeholder()
                return True

            idx = (idx + 1) % len(items)
        
        return False
    
    def __contains__(self, item):
        """
        Magic function responsible for checking if an item belongs to a set
        Invoked when "item in set" is executed.
        Returns True if an item is in a set and False otherwise.
        """
        idx = hash(item) % len(self.items)
        
        # loop to go through the items in the chain starting at hashed index
        while self.items[idx] != None:
            if self.items[idx] == item:
                return True
            
            idx = (idx + 1) % len(self.items)

        return False

    def __iter__(self):
        """
        Magic function responsible for iterating over items in set
        Invoked when "for item in set" is executed.
        """
        for i in range(len(self.items)):
            # only yield items that are not None or Placeholders
            if (self.items[i] != None) and (type(self.items[i]) != HashSet.__Placeholder):
                yield self.items[i]
                
    def __len__(self):
        """
        Magic function responsible for returning the length of a set
        Invoked when "len(set)" is executed
        """
        return self.numItems
    
    def add(self, item):
        """
        Function responsible for adding items into a set.
        Doubles items list size when load factor >= 75%.
        """
        if HashSet.__add(item, self.items):
            self.numItems += 1
            load = self.numItems / len(self.items)
            # double items list size of load factor >= 75%
            if load >= 0.75:
                self.items = HashSet.__rehash(self.items, [None]*2*len(self.items))

    def remove(self, item):
        """
        Function responsible for removing items from a set.
        Halves items list size when load factor <= 25%.
        In addition, raises an exception when item is not in a set.
        """
        if HashSet.__remove(item, self.items):
            self.numItems -= 1
            load = max(self.numItems, 10) / len(self.items)
            # halve items list size of load factor <= 25%
            if load <= 0.25:
                self.items = HashSet.__rehash(self.items, [None]*int(len(self.items)/2))
        else:
            raise KeyError("Item not in HashSet")

    def discard(self, item):
        """
        Function responsible for removing items from a set.
        Halves items list size when load factor <= 25%.
        Does not raise an exception when item is not in a set.
        """
        if HashSet.__remove(item, self.items):
            self.numItems -= 1
            load = max(self.numItems, 10) / len(self.items)
            if load <= 0.25:
                self.items = HashSet.__rehash(self.items, [None]*int(len(self.items)/2))
                
    def clear(self):
        """
        Function responsible for removing all elements of a set.
        Resets numItems instance variable to 0.
        Resets items instance variable with an empty list.
        """
        self.numItems = 0
        self.items = [None] * 10

    def update(self, other):
        """
        Function responsible for adding the items from one set to another set.
        """        
        for item in other:
            self.add(item)
            
    def difference_update(self, other):
        """
        Function responsible for subtracting from one set the elements of another set.
        A = A - B
        """  
        for item in other:
            self.discard(item)

    def difference(self, other):
        """
        Function responsible for subtracting from one set the elements of another set.
        C = A - B
        """
        result = HashSet(self)
        result.difference_update(other)
        
        return result

    def issuperset(self, other):
        """
        Function responsible for checking if one set is superset of another set
        Returns True if a set is a superset of another set and False otherwise.
        """
        for item in other:
            if item not in self:
                return False
            
        return True
    
