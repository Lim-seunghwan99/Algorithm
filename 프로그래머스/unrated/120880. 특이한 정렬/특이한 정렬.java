import java.util.Arrays;
class Solution {
    public int[] solution(int[] numlist, int n) {
        int[] answer = {};
        int[][] temp = new int[numlist.length][2];
        answer = new int[numlist.length];
        for (int i=0; i < numlist.length; i++){
            temp[i][0] = numlist[i];
            temp[i][1] = Math.abs(numlist[i] - n);
        }
        Arrays.sort(temp, (o1, o2) -> {
            return o1[1] != o2[1] ? o1[1]-o2[1] : o2[0] - o1[0];
        });
        // System.out.print(Arrays.deepToString(temp));
        for (int i=0; i < temp.length; i++){
            answer[i] = temp[i][0];
        }
        return answer;
    }
}