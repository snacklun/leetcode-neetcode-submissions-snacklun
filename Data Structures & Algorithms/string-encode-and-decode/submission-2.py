class Solution:

    def encode(self, strs: List[str]) -> str:
        string_encode = ""
        for index in strs:
            string_encode += str(len(index)) + "#" + index
        return string_encode
    def decode(self, s: str) -> List[str]:
        string_decode = []
        i = 0
        while i < len(s):
            length_str = ""
            while s[i].isdigit():    # ← keeps grabbing digits
                length_str += s[i]
                i += 1
            i += 1 # so it be in #
            number_length = int(length_str)
            extract_string = s[i:i + number_length]
            string_decode.append(extract_string)
            i = i + number_length
        return string_decode
