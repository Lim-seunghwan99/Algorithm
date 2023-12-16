import java.util.stream.IntStream;
class Solution {
    public int[] solution(int[] numbers, int num1, int num2) {
        // int[] answer = {};
        // answer = new int[num2 - num1 + 1];
        // int j = 0;
        // for(int i=num1; i<=num2; i++){
        //     answer[j] = numbers[i];
        //     j ++;
        // }
        return IntStream.rangeClosed(num1, num2).map(i -> numbers[i]).toArray();
    }
}