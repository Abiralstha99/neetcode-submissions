class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # We're using a stack 
        stack = []

        # Create a list with all the operators 
        operators = ['+','-','*','/']

        # Let's add the token into the stack and pop out the operands once
        # we reach a operator 

        for token in tokens:
            if token not in operators:
                # Since the tokens are in string, remember to convert back to int
                stack.append(int(token))
            else:
                # Now if it is in the opeators, we pop out from the stack
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                if token == '+':
                    result = operand_1 + operand_2
                if token == '-':
                    result = operand_1 - operand_2
                if token == '*':
                    result = operand_1 * operand_2
                if token == '/':
                    result = operand_1 / operand_2
                
                # After you calculate the result, push it back to the stack
                stack.append(int(result))
        
        # Now at the end, we just pop the top of the stack
        return stack.pop()
