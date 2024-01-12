import java.util.ArrayList;
import java.util.Arrays;
class Solution {
    public int[] solution(int[] arr, boolean[] flag) {
        int[] answer = {};
        ArrayList<Integer> arrlist = new ArrayList<>();
        
        for(int i=0; i < flag.length; i++){
            if(flag[i]){
                for(int j=0; j < arr[i]; j++) {
                    arrlist.add(arr[i]);
                    arrlist.add(arr[i]);
                }
            } else {
                for(int j=0; j < arr[i]; j++){
                    arrlist.remove(arrlist.size() - 1);
                }
            }
        }
        answer = new int[arrlist.size()];
        for(int i = 0; i < arrlist.size(); i++) {
            answer[i] = arrlist.get(i);
        }
        System.out.println(Arrays.toString(answer));
        return answer;
    }
}