import java.util.Arrays;
class Solution {
    public int solution(int n) {
        // int answer = 0;
        // String temp = Integer.toString(n);
        // for(int i=0; i < temp.length(); i++){
        //     answer += Integer.parseInt(temp.substring(i, i+1));
        // }
        // return answer;
        return Arrays.stream(String.valueOf(n).split("")).mapToInt(Integer::parseInt).sum();
    }
}