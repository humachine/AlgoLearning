#https://leetcode.com/problems/expression-add-operators/
''' Given a string that only contains digits 0-9 and a target, add any of the arithmetic operators (+-*) between digits so as to evaluate to the 'target'. Return all such possibilities.

    Inp: "123", 6
    Out: ["1+2+3", "1*2*3"] 

    Inp: '232', 8
    Out: ["2*3+2", "2+3*2"]

    Inp: '105', 5
    Out: ["1*0+5", "10-5"]

    Inp: "00", 0
    Out: ["0+0", "0-0", "0*0"]

    Inp: "3456237490", 9191
    Out: []
'''
class Solution(object):
    def findCombinations(self, startPos, currPath, currVal, multiplier, res):
        numStr, target = self.numStr, self.target
        if startPos == len(numStr): #If we have exhausted the entire input string
            if currVal == target: # If our current expression's evaluation = target, then we add it to our result
                res.append(''.join(currPath))
            return

        for i in xrange(startPos, len(numStr)):
            if i!=startPos and numStr[startPos] == '0': #We can't including numbers which have trailing zeros (except 0). Hence we return
                return

            curr = int(numStr[startPos:i+1])
            if startPos==0: # Check if we are starting first sequence
                currPath.append(str(curr))
                self.findCombinations(i+1, currPath, curr, curr, res) #If this is the first sequence, then just add it to the sequence and begin the backtracking search
                currPath.pop()
            else:
                # We try to see if we can reach the target by adding/subtracting/multiplying curr to the previous sum (i.e currVal)
                currPath.extend(['+', str(curr)]) #Add + and the current Number to the path
                self.findCombinations(i+1, currPath, currVal+curr, curr, res)

                currPath[-2] = '-' #Change the operation to minus
                self.findCombinations(i+1, currPath, currVal-curr, -curr, res)

                currPath[-2] = '*' #Change the operation to multiplication
                self.findCombinations(i+1, currPath, currVal-multiplier+multiplier*curr, multiplier*curr, res)
                #The multiplier argument tells us what the previous multiplier was, so that we can multiply curr with that and add it to result
                currPath.pop() #Pop twice to remove the sign and the current number (Backtracking step)
                currPath.pop()

    def addOperators(self, num, target):
        if not num: return []
        self.numStr, self.target = num, target
        res, currPath = [], []
        self.findCombinations(0, currPath, 0, 0, res)
        return res

s = Solution()
print s.addOperators('123', 6)
print s.addOperators('232', 8)
print s.addOperators('105', 5)
print s.addOperators('00', 0)
print s.addOperators('2326738423', 91919)
