import java.util.*;
class Solution {
    public int firstUniqChar(String s) {
        LinkedHashMap<Character,Integer>countchar=new LinkedHashMap<>();
        for(char c: s.toCharArray()){
            countchar.put(c,countchar.getOrDefault(c,0)+1);
        }
        char r;
        for(Map.Entry<Character,Integer> entry:countchar.entrySet()){
            if(entry.getValue()==1){
                return s.indexOf(entry.getKey());
            }
        }
        return -1;
    }
}