public class Solution {
   public int LengthOfLastWord(string s)
{
    s = s.TrimEnd(); // remove trailing spaces
    int lastSpace = s.LastIndexOf(' '); // find last space

    // slice from the last space to the end
    string lastWord = s[(lastSpace + 1)..];

    return lastWord.Length;
}
}
