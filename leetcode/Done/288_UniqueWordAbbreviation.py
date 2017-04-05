#https://leetcode.com/problems/unique-word-abbreviation/
'''An abbreviation of a word follows the form <first letter><number><last letter>. 
Given a dictionary and given a word, find whether its abbreviation is unique in the dictionary. 
A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

Input: [ "deer", "door", "cake", "card" ]
word = 'dear' 
Out: False

word = 'cart'
Out: True

word = 'cane'
Out: False

word = 'card'
Out: True
'''
class ValidWordAbbr(object):
    def _getAbbrev(self, word):
    # This function returns the abbreviation given a word
        if not word:
            abbrev = ''
        elif len(word) <= 2:
            abbrev = word[0] + word[-1]
        else:
            abbrev = word[0] + str(len(word)-2) + word[-1]
        return abbrev
    
    def __init__(self, dictionary):
        # We add the abbreviations of all words in the dictionary into a set of abbreviations
        self.abbrevs = {}
        for word in set(dictionary):
            abbrev = self._getAbbrev(word)
            # If the abbreviation is already in the dictionary, we update the
            # abbreviation to the counter 2 (denoting that 2 or more words in
            # the dictionary have the same abbreviation)
            if abbrev in self.abbrevs:
                self.abbrevs[abbrev] = '2'
            else:
            # If only one unique word in the dicationary has this abbreviation, 
            # the unique word is stored as the value.
                self.abbrevs[abbrev] = word

    def isUnique(self, word):
        # We just return if the abbreviation of the current word was seen in the dictionary.
        abbrev = self._getAbbrev(word)
        return abbrev not in self.abbrevs or self.abbrevs[abbrev] == word

s = ValidWordAbbr(["deer", "door", "cake", "card"])
for word in ['dear', 'cart', 'cane', 'make']:
    print s.isUnique(word)
