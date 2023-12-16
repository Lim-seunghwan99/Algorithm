import java.util.Arrays;
class Solution {
    public int solution(int[] array, int n) {
        int answer = 0;
        return (int)Arrays.stream(array).filter(i -> i == n).count();
    }
}