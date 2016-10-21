
public class NumArray {
    
    private int[] numbers;
    
    public NumArray(int[] nums) {
        // Need one extra space in array
        numbers = new int[nums.length+1];
        
        // iterates through all of nums
        // numbers has a padding of 0 at left.
        for (int i=0; i<nums.length; i++) {
            
            numbers[i+1] = nums[i] + numbers[i];
        }
        
    }
    

    public int sumRange(int i, int j) {
       int finalsum  = 0; 
       // j+1 because of extra padding 0 at numbers[0]
       // i because we want to include i+1 since its close bracketed
       finalsum = numbers[j+1]-numbers[i];
       return finalsum;
        
    }
}
