#https://leetcode.com/problems/arithmetic-slices/
"""
Return number of  arithmetic slices possible in array.
Arithmetic slice is a slice of array ATLEAST 3 length with all elements in an Arithmetic Progression.
An arithmetic slice is defined by (P, Q) representing starting & ending indices of elements

    Inp: [1, 2, 3, 4]
    Out: 3 ((0,2), (1,3), (0,3) corresponding to 123, 234, 1234)

    Inp: [7, 7, 7, 7, 7]
    Out: 6 ((0,4), (1,4), (0,3), (0,2), (1,3), (2,4))
"""
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        MIN_SLICE_LENGTH = 3
        if len(A) < MIN_SLICE_LENGTH:  return 0

        diff = A[1] - A[0]
        start = 0
        n = len(A)

        numSlices = 0
        for i in xrange(1, n):
            if A[i] - A[i-1] != diff:
                #Compute number of slices from start to i, if any
                sliceLen = i - start
                if sliceLen >= MIN_SLICE_LENGTH:
                    numSlices += ((sliceLen-2)*(sliceLen-1)/2)

                # Reset the difference values and reset start index of slice
                start = i-1
                diff = A[i] - A[i-1]

        # If sequence found at end of array
        sliceLen = len(A) - start
        if sliceLen >= MIN_SLICE_LENGTH:
            numSlices += ((sliceLen-2)*(sliceLen-1)/2)
        return numSlices
    
    def numberOfArithmeticSlicesConcise(self, A):
        MIN_SLICE_LENGTH = 3
        if len(A) < MIN_SLICE_LENGTH:  return 0

        numSlices = curr = 0
        for i in xrange(2, len(A)):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                #Beginning of a valid slice
                # Each time the slice length increases, we add sliceLen-2 to the answer (sliceLen-2 is denoted by curr)
                curr += 1
                numSlices += curr
            else:
                #curr counter set to zero since no slice possible
                curr = 0
        return numSlices

s = Solution()
print s.numberOfArithmeticSlicesConcise([1, 2, 3, 4])
print s.numberOfArithmeticSlicesConcise([7, 7, 7, 7, 7, 8, 9, 10])
print s.numberOfArithmeticSlicesConcise([7, 7, 7, 7, 7])
