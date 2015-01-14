class MinStack:
    def __init__(self):
    	self.stack = []
    	self.min = None

    # @param x, an integer
    # @return an integer
    def push(self, x):
    	if len(self.stack) == 0:
    		self.stack.append(0)
    		self.min = x
    	else:
    		self.stack.append(x-self.min)
    		if x < self.min:
    			self.min = x


    # @return nothing
    def pop(self):
    	if len(self.stack) == 0:
    		return
    	x = self.stack.pop()
    	if x < 0:
    		self.min -= x

        

    # @return an integer
    def top(self):
    	if len(self.stack) == 0:
    		return None
    	x = self.stack[-1]
    	if x < 0:
    		return self.min
    	else:
    		return self.min + x
        

    # @return an integer
    def getMin(self):
    	return self.min
        