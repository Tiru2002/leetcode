class Solution {
    public int lengthOfLongestSubstring(String s) {
        int l=0;
        
        for(int i=0;i<s.length();i++){
            HashSet<Character> set=new HashSet<>();
            for(int j=i;j<s.length();j++){
                if(set.contains(s.charAt(j))){
                    break;
                }
                set.add(s.charAt(j));
                 l=Math.max(l,set.size());
            }
           
        }
     return l;
    }
   
    }
