
import java.util.*;
class Solution {

    private static HashMap<String, Integer> create_counter(String s){
        HashMap<String, Integer> hm = new HashMap<>();
        for (String t: s.split(" ")){
            if (!hm.containsKey(t)) hm.put(t, 0);
            hm.replace(t, hm.get(t)+1);
        }
        return hm;
    }
    public String[] uncommonFromSentences(String s1, String s2) {
        HashMap<String, Integer> s1_count = create_counter(s1);
        HashMap<String, Integer> s2_count = create_counter(s2);

        String[] res = new String[s1_count.size() + s2_count.size()];
        int index = 0;

        for (String s : s1_count.keySet()){
            if(s1_count.get(s) < 2 && s2_count.getOrDefault(s, 0) == 0){
                res[index] = s;
                index++;
            }
        }
        for (String s : s2_count.keySet()){
            if(s2_count.get(s) < 2 && s1_count.getOrDefault(s, 0) == 0){
                res[index] = s;
                index++;
            }
        }

        return Arrays.copyOfRange(res, 0, index);
    }

    public static void main(String[] args){
        Solution obj = new Solution();
        String s1 = "z s s s z";
        String s2 = "s etj z";
        System.out.println(Arrays.toString(obj.uncommonFromSentences(s1, s2)));
    }
}
