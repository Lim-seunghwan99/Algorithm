class Solution {
    public int solution(String my_string) {
        int answer = 0;
        String[] arr = my_string.split("");
        String temp = "";
        for(int i=0; i<my_string.length(); i++){
            if(arr[i].matches("[0-9]")){
                temp += arr[i];
            } else {
                if(temp.isEmpty() == false){
                    answer += Integer.parseInt(temp);
                    temp = "";                   
                }
            }
        }
        if(temp.isEmpty() == false){
            answer += Integer.parseInt(temp);
            temp = "";
        }
        return answer;
    }
}