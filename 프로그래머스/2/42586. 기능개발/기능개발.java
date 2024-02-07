import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        int sv = 0; 
        int cnt = 0; 

        for (int i = 0; i < progresses.length; i++) {
            // 몫 + 1 값 구하는 로직!!
            int days = (100 - progresses[i] + speeds[i] - 1) / speeds[i];
            if (days > sv) {
                if (cnt > 0) {
                    // 이전까지의 배포 그룹을 결과에 추가
                    answer.add(cnt);
                }
                sv = days; 
                cnt = 1; 
            } else {
                cnt++;
            }
        }
        // 마지막
        answer.add(cnt);
        int[] ans = new int[answer.size()];
        for (int i = 0; i < answer.size(); i++){
            ans[i] = answer.get(i);
        }
        return ans;
    }
}
