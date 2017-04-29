#https://leetcode.com/problems/student-attendance-record-i/
'''Given a string with alphabet={P, A, L} representing Present, Absent and Late, 
determine if a student can be rewarded for his attendance record. 
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

Inp: PPALP
Out: True

Inp: PPALLL
Out: False  (More than 2 continous Ls)
'''
class Solution(object):
    def checkRecord(self, s):
        absent = late_streak = 0
        for rec in s:
            if rec == 'L':
                late_streak += 1
            else:
                late_streak = 0
                absent += int(rec == 'A')
            # If late streak hits 3 or 2 days of absence recorded, no reward
            if absent == 2 or late_streak == 3:
                return False
        return True

s = Solution()
print s.checkRecord('PPALP')
print s.checkRecord('PPALLL')
