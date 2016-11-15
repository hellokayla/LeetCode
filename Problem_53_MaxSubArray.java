import java.util.*;

public class Solution {
    public int maxSubArray(int[] nums) {
        
        // need two maximums
        int max_current = nums[0];
        int max_final = nums[0];
        
        // Compare curr_value w/ previous largest subset
        // max final keeps storing largest value
        for (int i = 1; i<nums.length; i++) {
            
            max_current = Math.max(nums[i], nums[i]+max_current);
            
            if (max_current > max_final)  {
                
                max_final = max_current; 
            }
            
        }
            return max_final;
    }

}