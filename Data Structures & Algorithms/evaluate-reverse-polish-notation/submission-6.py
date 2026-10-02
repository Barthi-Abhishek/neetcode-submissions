class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in "+*/-":
                stack.append(i)
            else:
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

            

        