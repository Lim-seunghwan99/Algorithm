import java.util.Arrays;
class Solution {
    public int[] solution(int[] arr, int k) {
        int[] answer = {};
        answer = new int[k];
        Arrays.fill(answer, -1);
        int temp = 0;
        for(int num : arr){
            if(chk(answer, num) && temp < answer.length){
                answer[temp] = num;
                temp++;
            }
        }
        return answer;
    }
    private boolean chk(int[] arr, int num){
        for (int i : arr){
            if (i == num) {
                return false;
            }
        }
        return true;
    }
}