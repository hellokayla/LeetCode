# Python program to print all permutations with 
# duplicates allowed 
  
def toString(List): 
    return ''.join(List) 
  
# Function to print permutations of string 
# This function takes three parameters: 
# 1. String 
# 2. Starting index of the string 
# 3. Ending index of the string. 
def permute(s, b_i, e_i): 
    if b_i==e_i: 
        print toString(s) 
    else: 
        for i in xrange(b_i,e_i+1): 
            s[b_i] = s[i]
            s[i] = s[b_i] 
            permute(s, b_i+1, e_i) 
            s[b_i], a[i] = a[i], a[b_i] # backtrack 
  
# Driver program to test the above function 
string = "ABC"
n = len(string) 
a = list(string) 
permute(a, 0, n-1) 