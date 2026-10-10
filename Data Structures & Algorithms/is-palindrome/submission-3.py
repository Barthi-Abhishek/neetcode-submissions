class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_withoutspaces = ""
        for i in s:
            if i.isalnum():
                s_withoutspaces += i.lower()
        i,j = 0, len(s_withoutspaces)-1
        while i < j:
            if s_withoutspaces[i].lower() != s_withoutspaces[j].lower():
                return False
            i = i+1
            j = j-1
        return True 






        