class Solution {
    public int solution(int left, int right) {
        int answer = 0;
        for (int i = left; i <= right; i++) {
            int sv = 0;
            for (int j=1; j <= i / 2; j++) {
                if (i % j == 0) {
                    sv++;
                }
            }
            if (sv % 2 == 1) {
                answer += i;
                
            } else {
                answer -= i;
            }
            // System.out.println(sv + " " + answer);
        }
        return answer;
    }
}