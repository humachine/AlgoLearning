#https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/
'''
'''
import random
from collections import defaultdict
class RandomizedCollection(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # vals has the list of values that are present in the collection
        # locs has the indices to the values that are present in the collection. Since duplicates are allowed, locs is a dictionary whose key is a number and value is a list of indices
        self.vals, self.locs = [], defaultdict(set)
        
    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.

        :type val: int
        :rtype: bool
        """
        # Add val to list of numbers
        self.vals.append(val)
        # Add location of val to the indices
        self.locs[val].add(len(self.vals)-1)
        return len(self.locs[val])==1
        
    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        # If val does not exist, nothing to remove
        if len(self.locs[val])==0:
            return False

        # Find the current location of this number (Of all possible locations for this number, randomly pop one out of th set)
        location = self.locs[val].pop()
        newVal = self.vals[-1]

        # Replacing the number with the last element of the list (i.e newVal)
        self.vals[location] = newVal
        # Deleting the last element of the list
        self.vals.pop()

        # We add the new location of newVal to its dictionary
        self.locs[newVal].add(location)
        # We also remove the old location (which was len(self.vals)) from the dictionary
        # Note: If we performed the remove first and then did the add, for the case where we remove the last element from the collectio:
        # i) We swap the last element with itself. And then we pop self.vals() leading us to an empty list
        # ii) We delete the old location of element(=len(self.vals)-1). We now add this location to the list of newVal (which incidentally happens to be the element itself). So now, self.locs[newVal] has one element which is 0 (for self.vals[0]). But self.vals is empty, leading to errors
        self.locs[newVal].remove(len(self.vals))

        return True
        
    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        # We randomly pick an element from the list
        return random.choice(self.vals)

s = RandomizedCollection()

print s.insert(1)
print s.insert(1)
print s.insert(2)
print s.insert(2)
print s.insert(2)
print 
print s.remove(1)
print s.remove(1)
print s.remove(2)
print 
print s.insert(1)
print s.remove(2)

print s.getRandom()
print s.getRandom()
print s.getRandom()
print s.getRandom()
print s.getRandom()
print s.getRandom()
print s.getRandom()
print s.getRandom()
print s.getRandom()
print s.getRandom()
