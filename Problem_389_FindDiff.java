public class Solution {
    public char findTheDifference(String s, String t) {
        
        // Find the letter generated 
        // Why don't we just find the difference
        
        char[] s_array = s.toCharArray();
        char[] t_array = t.toCharArray();
        char[] freqOfLetters = new char[26];
        char solution = '\0';
        
        for (int i = 0; i<s_array.length; i++) {
            
            freqOfLetters[s_array[i]-'a']++;
        }
        for (int j = 0; j<t_array.length; j++) {
            
            freqOfLetters[t_array[j]-'a']--;
        }
        
        for (int k = 0; k<freqOfLetters.length; k++) {
            
            if (freqOfLetters[k] > 0) {
                
                solution = (char)(k+97);
                
            }
        }
        
        return solution; 
    
    }
}