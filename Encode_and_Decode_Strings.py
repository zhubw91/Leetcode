class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        for s in strs:
            result += str(len(s)) + ',' + s
        return result

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        result = []
        state = 0
        length = 0
        temp = ""
        for word in s:
            if state == 0:
                if word == ',':
                    if length == 0:
                        result.append(temp)
                    else:
                        state = 1
                else:
                    length = length*10 + int(word)
            elif state == 1:
                temp += word
                if length > 1:
                    length -= 1
                else:
                    state = 0
                    result.append(temp)
                    length = 0
                    temp = ""
        return result




# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))