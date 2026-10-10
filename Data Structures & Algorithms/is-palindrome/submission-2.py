class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_withoutspaces = ""
        se="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        for i in s:
            if i != " " and i in se:
                s_withoutspaces = s_withoutspaces + i
        print(s_withoutspaces)
        i,j = 0, len(s_withoutspaces)-1
        print 
        while i < j:
            if s_withoutspaces[i].lower() != s_withoutspaces[j].lower():
                return False
            i = i+1
            j = j-1
        return True 






        