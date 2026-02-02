class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
                continue

            right_value = stack.pop()
            left_value = stack.pop()

            if token == "+":
                stack.append(left_value + right_value)
            elif token == "-":
                stack.append(left_value - right_value)
            elif token == "*":
                stack.append(left_value * right_value)
            else:  # "/"
                stack.append(int(left_value / right_value))

        return stack[-1]
