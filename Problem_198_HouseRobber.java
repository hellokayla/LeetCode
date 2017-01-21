import java.util.*;
public class Solution {
    public int rob(int[] nums) {

        int n = nums.length;
        int[] a1 = new int[n];
        
        // no houses to rob
        if (n == 0 || nums == null) { return 0;}
        
        // only one house to rob
        if (n==1) { return nums[0];}
        
        a1[0] = nums[0];
        a1[1] = Math.max(nums[0],nums[1]);
        
        for (int i = 2; i<nums.length; i++) {
                 
            a1[i]= Math.max(nums[i]+a1[i-2],a1[i-1]);
            System.out.println(a1[i]);
            
        }
        return a1[nums.length-1];
       
        
    }
}