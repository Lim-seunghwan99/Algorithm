import java.util.ArrayList;
class Solution {
    public int[][] solution(int[][] arr) {
        int mx = Math.max(arr.length, arr[0].length);
        int[][] answer = {};
        answer = new int[mx][mx];
        for(int i=0; i < arr.length; i++){
            for (int j=0; j < arr[i].length; j++){
                answer[i][j] = arr[i][j];
            }
        }
        return answer;
    }
}