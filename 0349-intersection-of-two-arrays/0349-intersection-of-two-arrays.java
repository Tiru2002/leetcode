class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
       HashSet<Integer> set1=new HashSet<>();
        HashSet<Integer> r=new HashSet<>();

       for(int n:nums1){
        set1.add(n);
       }
       for(int n:nums2){
        if(set1.contains(n)){
            r.add(n);
        }
        
       }
        int[] result = new int[r.size()];       
        int i=0;
       for(int n :r){
        result[i++]=n;
       }
       return result;
    }
}