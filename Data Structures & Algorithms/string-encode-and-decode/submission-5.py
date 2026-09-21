class Solution:
    

    def encode(self, strs: List[str]) -> str:
         st = ""
         for word in strs:
            st += str(len(word)) + "#" + word
         print (st)
         return st


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i<len(s):
            j = i
            # finding the delimiter
            while s[j] != "#":
                j = j+1
            # counting the length
            length = int(s[i:j])

            # move past the #
            i = j+1
            # read the word
            word = s[i:i+length]
            result.append(word)

            # adjusting the i value based on the lenght 
            i = i+length
        return result


            
            
            
            

        
