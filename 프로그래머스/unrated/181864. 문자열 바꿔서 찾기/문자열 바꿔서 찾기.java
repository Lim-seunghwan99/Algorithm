import java.util.Arrays;
class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        String[] arr = pat.split("");
        for(int i=0; i < arr.length; i++){
            if(arr[i].equals("A")){
                arr[i] = "B";
            } else {
                arr[i] = "A";
            }
        }
        String str = String.join("", arr);
        System.out.println(str);
        return myString.contains(str) ? 1 : 0;
    }
}