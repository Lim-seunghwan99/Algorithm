class Solution {
    public int solution(int n) {
        int answer = 0;
        answer = (int)Math.ceil(n/7);
        if(n%7 > 0){
            answer += 1;
        }
        return answer;
    }
}