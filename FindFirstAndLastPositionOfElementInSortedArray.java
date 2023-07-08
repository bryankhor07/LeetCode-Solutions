class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] position = new int[2];
		
		    int n = nums.length;
		    int first = -1, last = -1;
		    for (int i = 0; i < n; i++) {
			    if (target != nums[i])
				    continue;
			    if (first == -1)
				    first = i;
			    last = i;
		    }
		
		    position[0] = first;
		    position[1] = last;
		
		    return position;
    }
}
