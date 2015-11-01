class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        l = len(words)
        tmp_result = []
        cur_l = 0
        for word in words:
        	if cur_l + len(tmp_result) + len(word) <= maxWidth:
        		cur_l += len(word)
        		tmp_result.append(word)
        	else:
        		# justification
        		space_num = maxWidth - cur_l
        		tmp_s = ""
        		if len(tmp_result) == 1:
        			tmp_s = tmp_result[0] + " "*space_num
        		else:
        			space_num_each = space_num/(len(tmp_result)-1)
        			space_num_r = space_num%(len(tmp_result)-1)
        			for i in range(len(tmp_result)-1):
        				if i < space_num_r:
        					tmp_s += tmp_result[i] + " "*(space_num_each+1)
        				else:
        					tmp_s += tmp_result[i] + " "*space_num_each
        			tmp_s += tmp_result[-1]
        		result.append(tmp_s)
        		tmp_result = [word]
        		cur_l = len(word)
        if len(tmp_result) > 0:
        	tmp_s = " ".join(tmp_result)
        	tmp_s += " "*(maxWidth-cur_l-len(tmp_result)+1)
        	result.append(tmp_s)
        return result