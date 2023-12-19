class Solution {
    public int solution(int num, int k) {
        String temp = String.valueOf(num);
        int answer = temp.indexOf(String.valueOf(k));
        if(answer != -1){
            answer += 1;
        }
        return answer;
    }
}