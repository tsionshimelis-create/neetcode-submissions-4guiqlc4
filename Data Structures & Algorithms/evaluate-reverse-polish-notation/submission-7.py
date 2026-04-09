class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "*", "-", "/"}

        stack = []

        res = 0

        for i in range(len(tokens)):
            if tokens[i] in operators:
                
                op2 = stack.pop()
                op1 = stack.pop()
                if tokens[i] == "+":
                    res = op1 + op2
                elif tokens[i] == "*":
                    res = op1 * op2
                elif tokens[i] == "-":
                    res = op1 - op2
                else:
                    if op2 == 0:
                        return -1

                    res = int(op1 / op2)
                stack.append(res)
            else:
                stack.append(int(tokens[i]))


        return stack[0]