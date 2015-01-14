class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        def equals(s,p,i,j):
            if (s[i] == p[j] or p[j] == '.'):
                return True
            else:
                return False
        m = len(s)
        n = len(p)
        if s == None and p == None:
            return False
        OPT = [[False for i in range(n+1)] for j in range(m+1)]
        OPT[0][0] = True
        for i in range(1,m+1):
            OPT[i][0] = False
        for j in range(1,n+1):
            OPT[0][j] = p[j-1] == '*' and j-2 >= 0 and OPT[0][j-2]
        for i in range(1,m+1):
            for j in range(1,n+1):
                OPT[i][j] = (OPT[i-1][j-1] and equals(s,p,i-1,j-1)) or \
                ((OPT[i][j-1] or OPT[i-1][j]) and p[j-1] == '*' and equals(s,p,i-1,j-2)) or \
                    (p[j-1] == '*' and (j-2>=0) and OPT[i][j-2])
        return OPT[m][n]
