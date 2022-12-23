class Solution {
    public boolean isPalindrome(String s) {
        String str="";
        for(char i:s.toCharArray())
        {
            if(Character.isAlphabetic(i) || Character.isDigit(i))
            {
                str+=Character.toLowerCase(i);
            }
        }
        System.out.print(str);
        char strArr[]=str.toCharArray();
        for(int i=0,j=str.length()-1;i<str.length()/2;i++,j--)
        {
        if(strArr[i]!=strArr[j])
        {
        return false;
        }
        }
        return true;
    }
}
