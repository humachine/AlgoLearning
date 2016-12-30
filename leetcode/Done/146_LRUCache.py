#https://leetcode.com/problems/lru-cache/
''' Implement an LRU Cache '''

from collections import OrderedDict
class LRUCache(object):
    ''' An ordered dict preserves the order in which elements are inserted into the dictionary. 
    Also an ordered dict supports popping the least recently (and also most recently) inserted element. 
    We exploit this property to simulate an LRU cache.

    OrderedDicts are implemented using linked lists.
    '''
    def __init__(self, capacity):
        self.data = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        dic = self.data
        # If key is not available in dictionary, return -1
        if key not in dic:
            return -1
        # Store the value that needs to be returned
        val = dic[key]

        # We need to bring this key and make it the most recently used key
        # To perform that we delete the original entry and add it again into the cache (this time it gets added as the most recently inserted element)
        del dic[key]
        dic[key] = val
        return val

    def set(self, key, value):
        dic = self.data
        # If just perform a dic[key] = value, the ordering of dic[key] is still retained from its original insertion order.
        # Eg: We insert (1,1), (2,2), (3,3), (4,4) into the dict. Now, we wish to insert (2, 4) into the cache. 
        # Performing dict[2] = 4 maintains the same ordering [(2,4) will continue to be the second least recently inserted element]
        if key in dic:
            del dic[key]
        # If we have a capacity issue, we pop the least recently/oldest inserted element.
        if len(dic) == self.capacity:
            dic.popitem(last = False) #If last=True, it pops out in a FIFO order. last=False ensures LIFO popping
        dic[key] = value
