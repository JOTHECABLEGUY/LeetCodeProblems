/*432. All O`one Data Structure
Hard
Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the AllOne class:

AllOne() Initializes the object of the data structure.
inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
Note that each function must run in O(1) average time complexity.


Example 1:

Input
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
Output
[null, null, null, "hello", "hello", null, "hello", "leet"]

Explanation
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "hello"
allOne.inc("leet");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "leet"

Constraints:

1 <= key.length <= 10
key consists of lowercase English letters.
It is guaranteed that for each call to dec, key is existing in the data structure.
At most 5 * 104 calls will be made to inc, dec, getMaxKey, and getMinKey.
 */

import java.util.*;
class AllOne {
    private HashMap<String, Integer> hm;
    private HashSet<String> keys;
    private String min_key;
    private String max_key;
    public AllOne() {
        this.hm = new HashMap<>();
        this.keys = new HashSet<>();
        this.min_key = "";
        this.max_key = "";
    }
    
    public void inc(String key) {
        if (this.keys.contains(key)) {
            this.hm.put(key, this.hm.get(key) + 1);
            if (this.hm.get(key) > this.hm.get(this.max_key)) this.max_key = key;
            if (key.equals(this.min_key)){
                for(Map.Entry<String, Integer> entry : this.hm.entrySet()){
                    if (entry.getValue() < this.hm.get(key)){
                        this.min_key = entry.getKey(); 
                        break;
                    }
                }
            }
        }
        else{
            this.hm.put(key, 1);
            this.keys.add(key);
            this.min_key = key;
            if (this.keys.size() == 1) this.max_key = key;
        }
    }
    
    public void dec(String key) {
        if (this.keys.contains(key)) {
            this.hm.put(key, this.hm.get(key) - 1);
            int val = this.hm.get(key);
            if (val <= 0) {
                this.hm.remove(key);
                this.keys.remove(key);
                if (key.equals(this.min_key)){
                    if (this.keys.isEmpty()){this.min_key = ""; return;}
                    int min_val = Integer.MAX_VALUE;
                    for(Map.Entry<String, Integer> entry : this.hm.entrySet()){
                        if (entry.getValue() < min_val){ 
                            min_val = entry.getValue(); 
                            this.min_key = entry.getKey();
                        }
                    }
                }
            }
            if (this.max_key.equals(key)){
                int max_val = Integer.MIN_VALUE;
                for(Map.Entry<String, Integer> entry : this.hm.entrySet()){
                    if (entry.getValue() > max_val){ 
                        max_val = entry.getValue(); 
                        this.max_key = entry.getKey();
                    }
                }
            }
            if (val > 0 && val < this.hm.get(this.min_key)) this.min_key = key;
        }
    }
    
    public String getMaxKey() {
        return this.max_key;
    }
    
    public String getMinKey() {
        return this.min_key;
    }
}

/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne obj = new AllOne();
 * obj.inc(key);
 * obj.dec(key);
 * String param_3 = obj.getMaxKey();
 * String param_4 = obj.getMinKey();
 */
