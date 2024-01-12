import java.util.Arrays;
class Solution {
    public String solution(String my_string, int[] indices) {
        String answer = "";
        String[] arr = my_string.split("");
        for(int index : indices){
            arr[index] = "";
        }
        System.out.print(Arrays.toString(arr));
        answer = String.join("", arr);
        return answer;
    }
}