class Solution {
    public String[] solution(String my_str, int n) {
        String[] answer = {}; 
        int cnt = (my_str.length() + n - 1) / n;
        answer = new String[cnt];
        for(int i = 0; i < cnt; i++){
            int start = n * i;
            int end = 0;
            if(start + n >= my_str.length()){
                end = my_str.length();
            } else {
                end = start + n;
            }
            answer[i] = my_str.substring(start, end);
        }
        return answer;
    }
}