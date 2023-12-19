class Solution {
    public int solution(int num, int k) {
        int answer = -1;
        String temp = Integer.toString(num);
        int[] digits = new int[temp.length()];
        for(int i=0; i< temp.length(); i++){
            if((temp.charAt(i) - '0') == k){
                answer = i + 1;
                break;
            }
        }
        return answer;
    }
}