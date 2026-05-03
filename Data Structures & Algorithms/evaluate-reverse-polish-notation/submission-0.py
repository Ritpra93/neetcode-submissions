class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t)) #you know its not an operator
            else:
                r,l = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(l+r)
                elif t == "-":
                    stack.append(l-r)
                elif t == "*":
                    stack.append(l*r)
                else: #division is a little weird
                    stack.append(int(float(l/r)))
        return stack.pop()
        #float division equals zero that's important



        