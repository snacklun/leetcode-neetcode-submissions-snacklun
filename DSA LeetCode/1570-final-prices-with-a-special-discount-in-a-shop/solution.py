class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = []
        for index, value in enumerate(prices):
            stack = []
            for index_smaller_loop in range(len(prices) - 1, index, -1):
                new_value = prices[index_smaller_loop]
                while stack and stack[-1] >= new_value:
                    stack.pop()
                if(new_value <= value):
                    stack.append(new_value)
            
            if stack:
                result.append(value - stack.pop())
            else:
                result.append(value)


        return result
