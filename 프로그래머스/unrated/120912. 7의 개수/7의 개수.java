import java.util.Arrays;
class Solution {
    public int solution(int[] array) {
        int answer = 0;
        for(int i = 0; i<array.length; i++){
            String num = Integer.toString(array[i]);
            System.out.print(num);
            String[] arr = num.split("");
            for(int j = 0; j < arr.length; j++){
                if(arr[j].equals("7")){
                    answer++;
                }
            }
        }
        return answer;  
    }
}