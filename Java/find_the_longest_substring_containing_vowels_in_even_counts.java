import java.util.*;

class Solution {

    public int findTheLongestSubstring(String s) {
        int mask = 0;
        HashMap<Integer, Integer> memo = new HashMap<>();
        memo.put(0, -1);
        int result = 0;
        for (int i = 0; i < s.length(); i++){
            switch (s.charAt(i)) {
                case 'a': mask = mask ^ 1; break;
                case 'e': mask = mask ^ 1 << 1; break;
                case 'i': mask = mask ^ 1 << 2; break;
                case 'o': mask = mask ^ 1 << 3; break;
                case 'u': mask = mask ^ 1 << 4; break;
                default: break;
            }
            if (memo.get(mask) != null) result = Math.max(result, i - memo.get(mask));
            else memo.put(mask, i);
        }
        return result;
    }
    public static void main(String[] args){
        String s1 = "eleetminicoworoep";
        String s2 = "leetcodeisgreat";
        String s3 = "bcbcbc";
        Solution obj = new Solution();
        System.out.println("Found " + obj.findTheLongestSubstring(s1) + " Expected " + 13);
        System.out.println("Found " + obj.findTheLongestSubstring(s2) + " Expected " + 5);
        System.out.println("Found " + obj.findTheLongestSubstring(s3) + " Expected " + 6);
    }
}
