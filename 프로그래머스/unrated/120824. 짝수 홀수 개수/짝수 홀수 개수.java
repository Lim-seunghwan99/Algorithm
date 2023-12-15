import java.util.Arrays;
import java.util.stream.IntStream;
class Solution {
    public int[] solution(int[] num_list) {
        // int[] answer = new int[2];
        // int odd = 0;
        // int even = 0;
        // for(int i = 0; i < num_list.length; i++){
        //     if(num_list[i] % 2 == 0){
        //         even ++;
        //     } else {
        //         odd ++;
        //     }
        // }
        // answer[0] = even;
        // answer[1] = odd;
        // return answer;
        return IntStream.of((int) Arrays.stream(num_list).filter(i -> i%2 == 0).count(), 
                            (int) Arrays.stream(num_list).filter(i -> i % 2 ==1).count()).toArray();
    }
}