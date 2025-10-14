public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        if (strs == null || strs.Length == 0)
            return string.Empty;

        if (strs.Length == 1)
            return strs[0] ?? string.Empty;


        var result = CommonString(strs[0], strs[1]);
        for (int i = 0; i < strs.Length - 1; i++)
        {
          var temp = CommonString(strs[i], strs[i+1]);
          if (result.Contains(temp))
          {
            result = temp;
          }
        }
        return result;
    }

    public string CommonString(string a, string b)
    { if (string.IsNullOrEmpty(a) || string.IsNullOrEmpty(b))
            return string.Empty;

        int minLen = Math.Min(a.Length, b.Length);
        int i = 0;
        // advance while characters match
        while (i < minLen && a[i] == b[i])
        {
            i++;
        }

        // substring from 0..i (i is first mismatch or minLen)
        return a.Substring(0, i);
    }
}
