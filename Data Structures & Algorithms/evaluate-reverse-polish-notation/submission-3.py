class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens)==1:
            return int(tokens[0])
        stack = []
        signs = {'+', '-', '*', '/'}
        for i in range(len(tokens)):
            if tokens[i] not in signs:
                stack.append(int(tokens[i]))
            else:
                temp2 = stack.pop()
                temp1 = stack.pop()
                if tokens[i]=='+':
                    stack.append(temp1+temp2)
                elif tokens[i]=='-':
                    stack.append(temp1-temp2)
                elif tokens[i]=='*':
                    stack.append(temp1*temp2)
                elif tokens[i]=='/':
                    stack.append(int(temp1/temp2))
        return stack[0]
        