public class Solution {
    public int maxProfit(int[] prices) {
                
        int lowest = Integer.MAX_VALUE;
        int profit = 0;
        int maxProfit = 0; 
        
        if (prices == null || prices.length == 0) { return 0;}
        
        for (int i = 0; i<prices.length; i++) {
			
            lowest = Math.min(lowest, prices[i]);
            
            profit = prices[i] - lowest;
            
            maxProfit = Math.max(maxProfit, profit);
        }
       
        return maxProfit; 
    }
}