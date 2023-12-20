import java.util.Arrays;
import java.util.Collections;
class Solution {
    public int[] solution(int[] emergency) {
        int[] answer = {};
        answer = new int[emergency.length];
        // Collections.reverseOrder()는 Integer 배열에서만 가능하다.
        Integer[] temp = new Integer[emergency.length];
        for(int i=0; i<emergency.length; i++){
            temp[i] = emergency[i];
        }
        Arrays.sort(temp, Collections.reverseOrder());
        System.out.println(Arrays.toString(temp));
        System.out.println(Arrays.toString(emergency));
        for(int i=0; i<temp.length; i++){
            for(int j=0; j<emergency.length; j++){
                if(temp[i] == emergency[j]){
                    answer[j] = i + 1;
                }
            }
        }
        return answer;
    }
}