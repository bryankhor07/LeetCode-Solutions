// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int i = 0;
        int j = 1;

        while (true) {
            if (nums[i] + nums[j] == target) {
                return new int[] {i, j};
            } else {
                if (j != nums.length - 1) {
                    j++;
                } else {
                    i++;
                    j = i + 1;
                }
            }
        }
    }
}
