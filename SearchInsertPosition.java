// Given a sorted array of distinct integers and a target value, return the index if the target is found. 
// If not, return the index where it would be if it were inserted in order.

class Solution {
    public int searchInsert(int[] nums, int target) {
        int index = 0;
		
		    for (int i = 0; i < nums.length; i++) {
			    if (nums[i] == target) {
				    index = i;
				    break;
			    }
			    if (target > nums[nums.length - 1]) {
				    index = nums.length;
				    break;
			    }
			    if (target > nums[i] && target < nums[i + 1]) {
				    index = i + 1;
				    break;
			    } 
		    }
		
		
		    return index;
    }
}
