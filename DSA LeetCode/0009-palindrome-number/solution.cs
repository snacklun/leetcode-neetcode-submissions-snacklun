public class Solution {
    public bool IsPalindrome(int x) {
        var chars = x.ToString().ToCharArray();
        for(int i = 0; i < chars.Length/2; i++)
        {
            var temp = i+1;
            if(chars[i] != chars[chars.Length - temp])
            {
              return false;
            }
        }
        return true;
    }
}
