class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        num_hash = {}
        for i in range(len(secret)):
        	if secret[i] not in num_hash:
        		num_hash[secret[i]] = 0
        	num_hash[secret[i]] += 1
        bull,cow = 0,0
        for i in range(len(guess)):
        	if guess[i] == secret[i]:
        		bull += 1
        		num_hash[guess[i]] -= 1
        
        for i in range(len(guess)):
        	if guess[i] != secret[i] and guess[i] in num_hash and num_hash[guess[i]] > 0:
        		cow += 1
        		num_hash[guess[i]] -= 1
        return str(bull)+"A"+str(cow)+"B"
