class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        int sv = 0;
        for(int i=0; i< numbers.length; i++){
            sv += numbers[i];
        }
        answer = (double)sv / numbers.length;
        return answer;
    }
}