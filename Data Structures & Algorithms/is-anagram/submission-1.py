class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s_list = list(s)
        # t_list = list(t)
        # s_list.sort()
        # t_list.sort()
        # if s_list == t_list:
        #     return True
        # return False      
        if len(s) != len(t):
            return False

        countS = {}
        countT = {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)  
            countT[t[i]] = 1 + countT.get(t[i],0)  
        
        return countS == countT