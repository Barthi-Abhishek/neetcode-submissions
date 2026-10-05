class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result =[0]*len(temperatures)
        stack =[]
        for i,temp in enumerate(temperatures):
            while stack:
                prev_i, prev_temp = stack[-1]
                if prev_temp < temp:
                    result[prev_i] = i-prev_i 
                    stack.pop()
                else:
                    break
            stack.append((i, temp))
        return result

            
                

        