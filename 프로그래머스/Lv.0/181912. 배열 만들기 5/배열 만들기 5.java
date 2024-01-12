import java.util.ArrayList;
import java.util.Arrays;
class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        int[] answer = {};
        ArrayList<Integer> arr = new ArrayList<>();
        for(String a : intStrs){
            int temp = Integer.parseInt(a.substring(s, s+l));
            if(temp > k){
                arr.add(temp);
            }
        }
        answer = new int[arr.size()];
        for(int i=0; i < arr.size(); i++){
            answer[i] = arr.get(i);
        }
        System.out.println(Arrays.toString(answer));
        return answer;
    }
}