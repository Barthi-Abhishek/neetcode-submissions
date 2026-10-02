class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        see = set(("+","-","*","/"))
        for i in tokens:
            if i not in see:
                stack.append(i)
            elif len(stack) >= 2:
                if i == "+":
                    stack.append(int(stack.pop()) + int(stack.pop()))
                elif i == "-":
                    num2 = int(stack.pop())
                    stack.append(int(stack.pop()) - num2)
                elif i == "*":
                    stack.append(int(stack.pop()) * int(stack.pop()))
                else:
                    num3 = int(stack.pop())
                    stack.append(int(stack.pop()) / num3)
        return int(stack[-1])

            

        