#https://leetcode.com/problems/insert-delete-getrandom-o1/
'''
'''
import random
class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals, self.locs = [], {}
        
    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        # If value already in set, then return False
        if val in self.locs:
            return False
        # Else, add value to end of vals and update locs with its location
        self.vals.append(val)
        self.locs[val] = len(self.vals)-1
        return True
        
    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        # If val does not exist, nothing to remove
        if val not in self.locs:
            return False
        # Find the current location of this number
        location = self.locs[val]
        newVal = self.vals[-1]

        # Swapping current number with the last number
        self.vals[location] = newVal
        self.locs[newVal] = location

        # Removing val from both locs and vals
        self.vals.pop()
        self.locs.pop(val)
        return True
        
    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        randIndex = random.randint(0, len(self.vals)-1)
        return self.vals[randIndex]
        
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
