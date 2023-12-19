import java.util.stream.IntStream;
class Solution {
    public int[] solution(int n) {
        // return IntStream.rangeClosed(1, n).filter(i -> n % i == 0).toArray();
        int[] answer = {};
        answer = new int[n];
        int cnt = 0;
        for(int i=1; i <= n; i++){
            if(n % i == 0){
                cnt++;
            }
        }
        answer = new int[cnt];
        cnt = 0;
        for(int i=1; i <= n; i++){
            if(n % i == 0){
                answer[cnt] = i;
                cnt++;
            }
        }
        return answer;
    }
}