import java.util.Arrays;
class Solution {
    public int solution(int[][] dots) {
        int answer = 0;
        Arrays.sort(dots, (o1, o2) -> {
            return o1[0] - o2[0];
        });
        System.out.println(Arrays.deepToString(dots));
        int x = Math.abs(dots[3][0] - dots[0][0]);
        Arrays.sort(dots, (o1, o2) -> {
            return o2[1] - o1[1];
        });
        System.out.print(Arrays.deepToString(dots));
        int y = Math.abs(dots[0][1] - dots[3][1]);
        answer = x * y;
        return answer;
    }
}