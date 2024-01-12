import java.util.Arrays;
class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = {};
        answer = new int[arr.length];
        int n = queries.length;
        for(int i=0; i < n; i++){
                int temp = arr[queries[i][0]];
                arr[queries[i][0]] = arr[queries[i][1]];
                arr[queries[i][1]] = temp;
        }
        // System.out.println(Arrays.toString(arr));
        answer = arr;
        return answer;
    }
}