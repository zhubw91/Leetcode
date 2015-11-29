public class Solution {
    public int numDistinct(String s, String t) {
    	int[][] f = new int[s.length()+1][t.length()+1];
    	for(int i = 0;i <= s.length();i++)
    	{
    		f[i][0] = 1;
    	}
    	for(int j = 0;j <= t.length()-1;j++)
    	{
    		for(int i = 0;i <= s.length()-1;i++)
    		{
    			if(s.charAt(i) == t.charAt(j))
    			{
    				f[i+1][j+1] = f[i][j+1] + f[i][j];
    			}
    			else
    			{
    				f[i+1][j+1] = f[i][j+1];
    			}
    		}
    	}
    	return f[s.length()][t.length()];
        
    }
}