class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if(len(s)!=len(goal)):
            return False
        string=s+s
        return goal in string
      
