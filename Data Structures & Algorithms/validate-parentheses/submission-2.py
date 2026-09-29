class Solution:
    def isValid(self, s: str) -> bool:
        #vaid means use set or hashamap 
        #for this we use hashmap we have track the two bracktes
        stack = []
        brack = {'}':'{', ')':'(',']':'['}
        for i in s:
            if i not in brack:
                stack.append(i)
            elif not stack:
                return False
            elif stack.pop()!= brack[i]:
                return False
        if not stack:
            return True
        else:
            return False


            
        