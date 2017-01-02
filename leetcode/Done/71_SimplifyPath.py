#https://leetcode.com/problems/simplify-path/
''' Given a Unix-style path, simplify it.
    
    Inp: "/home/"
    Out: "/home"

    Inp: "/a/../b/../../c/"
    Out: "/c" (From directory /, /a + .. + /b + .. brings us back to / and / + .. -> / and lastly / + /c brings us to /c)
'''
class Solution(object):
    def simplifyPath(self, path):
        # We first get a list of directory changes that is present in this path by splitting on '/'
        # We ignore any splits that are = '.' (/abc/./def/ghe) to ignore the ./ of current directory
        # We also ignore any empty splits which happen when we have multiple consecutive / together
        
        dirs = [pt for pt in path.split('/') if pt not in ['.', '']]
        st = []
        # We build a stack of directories. Every time we see a directory, we go deeper a level into the file system. Every time we see a '..', we pop the stack thereby going back a level lower.
        for dir in dirs:
            if dir == '..':
                if len(st)>0:
                    st.pop()
            else:
                st.append(dir)
        # Finally, we return / + all the relevant directories slash-separated
        return '/' + '/'.join(st)
s = Solution()
print s.simplifyPath("/a/../b/../../c/")
print s.simplifyPath("/../")
print s.simplifyPath("/a///.b/c/")
print s.simplifyPath("/..")
