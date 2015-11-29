public class NumArray {

	int cul[];
    public NumArray(int[] nums) {
    	cul = new int[nums.length];
    	if(nums.length >= 1) cul[0] = nums[0];
    	for(int i=1;i<=nums.length-1;i++)
    	{
    		cul[i] = cul[i-1] + nums[i];
    	}
        
    }

    public int sumRange(int i, int j) {
    	if(i == 0)
    	{
    		return cul[j];
    	}	
    	else
    	{
    		return cul[j] - cul[i-1];
    	}
    }
}


// Your NumArray object will be instantiated and called as such:
// NumArray numArray = new NumArray(nums);
// numArray.sumRange(0, 1);
// numArray.sumRange(1, 2);