class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        check_set = set()
        for index in range(len(sentence)):
            if (sentence[index] not in check_set):
                check_set.add(sentence[index])
                
        if (len(check_set) == 26):
            return True
        return False
