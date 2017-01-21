public class Solution {
    public String reverseVowels(String s) {
        // Convert the string to separate Characters
        char [] charArray = s.toCharArray();
        String stringReturn = ""; 

        // need this to initialize to a changing array
        List<Character> charArrayRev = new ArrayList<Character>(); 
        
        for (int i=0; i < charArray.length; i++) {
            
            if ( charArray[i] == 'a' ||
                 charArray[i] == 'A' ||
                 charArray[i] == 'e' ||
                 charArray[i] == 'E' ||
                 charArray[i] == 'I' ||
                 charArray[i] == 'i' ||
                 charArray[i] == 'O' ||
                 charArray[i] == 'o' ||
                 charArray[i] == 'U' ||
                 charArray[i] == 'u' )    {
            
               // Create a new array for reversing...
               charArrayRev.add(charArray[i]);
               
               // Replace '*' for each vowel...
               charArray[i] = '*';
            }
               
        }

        
        Collections.reverse(charArrayRev);
        System.out.println(charArrayRev);

        
        // Take all of charArrayRev and place back into charArray...
        
        for ( int k = 0; k < charArray.length; k++) {
           if  ( charArray[k] == '*' ) {
                 //for (int i = 0; i<charArrayRev.size(); i++) {
                      
                      charArray[k] = charArrayRev.get(0);
                      charArrayRev.remove(0);
                 //}
           }
        }
        
        stringReturn = String.valueOf(charArray);
        //System.out.println(stringReturn);
        return stringReturn;

        
    }
}