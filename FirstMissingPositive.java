class Solution {
    public int firstMissingPositive(int[] nums) {
        boolean[] vals = new boolean[nums.length + 1];
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] < nums.length + 1 && nums[i] >= 0) {
                vals[nums[i]] = true; 
            }
        }
        for (int i = 0; i < vals.length; i++) {
            if (vals[i] == false && i > 0) {
                System.out.println(i);
                return i;
            }
        }
        return vals.length;
    }
}