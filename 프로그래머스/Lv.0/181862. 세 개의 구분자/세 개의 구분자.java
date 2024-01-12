import java.util.Arrays;
import java.util.ArrayList;
class Solution {
    public String[] solution(String myStr) {
        String[] answer = {};
        ArrayList<String> arrList = new ArrayList<>();
        String[] arr = myStr.split("[abc]");
        for(int i=0; i < arr.length; i++){
            if(!arr[i].isBlank()){
                arrList.add(arr[i]);
            }
        }
        if(arrList.size() > 0){
            answer = new String[arrList.size()];
            for(int i=0; i < arrList.size(); i++) {
                answer[i] = arrList.get(i);
            }
        } else {
            answer = new String[1];
            answer[0] = "EMPTY";
        }
        return answer;
    }
}