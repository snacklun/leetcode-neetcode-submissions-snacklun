class Solution:
    def isValid(self, s: str) -> bool:
        valid_parenthese = []
        for value in s:
            if value in "({[":
                valid_parenthese.append(value)
            else: 
                if len(valid_parenthese) > 0:
                    if value == ")" and valid_parenthese[-1] != "(":
                        return False
                    if value == "]" and valid_parenthese[-1] != "[":
                        return False
                    if value == "}" and valid_parenthese[-1] != "{":
                        return False
                    valid_parenthese.pop()
                else:
                    return False
        if len(valid_parenthese) > 0:
            return False
        return True
