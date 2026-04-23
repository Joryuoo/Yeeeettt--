class Solution {
    public boolean isPalindrome(int x) {
        int rev = 0;
        int cp = x;
        while(cp > 0){

            // 121 % 10 = 1
            // 121 / 10 =  12
            // (0 * 10) + 1 = 1
            // 12 % 10 = 2
            // 12 / 10 = 1
            // (1 * 10) + 2 = 12
            // 1 % 10 = 1
            // 1 / 10 = 0
            // (12 * 10) + 1 = 121 
            
            int rem = cp % 10;
            rev = (rev * 10) + rem;
            //update
            cp /= 10; 
        }
        return x == rev;
    }
}