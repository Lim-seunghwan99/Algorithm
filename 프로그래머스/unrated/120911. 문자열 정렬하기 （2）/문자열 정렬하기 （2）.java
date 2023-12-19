import java.util.Arrays;
class Solution {
    public String solution(String my_string) {
        String answer = "";
        String[] temp = my_string.toLowerCase().split("");
        Arrays.sort(temp);
        return String.join("", temp);
    }
}