class Solution {
    public String solution(String myString, String pat) {
        String answer = "";
        for(int i=myString.length(); i >= 3; i--){
            if(myString.substring(0, i).endsWith(pat)){
                answer = myString.substring(0, i);
                return answer;
            }
        }
        return answer;
    }
}