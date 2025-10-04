class Solution {
    public int lengthOfLastWord(String s) {
        String []str=s.split(" ");
        String l=str[str.length-1];

        return l.length();
    }
}