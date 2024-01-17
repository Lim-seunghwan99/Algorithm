import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        int cnt = 0;
        // 한 번에 한 개의 알파벳만 바꿀 수 있다.
        // words에 있는 단어로만 변환할 수 있다.
        // bfs로 푸는게 좋다.
        // begin이 words안에 있으면 계속 반복한다, 사용한 단어 체크해야함
        // works의 방문체크는 하면 안된다.
        Queue<String> q = new LinkedList<>();
        q.add(begin);

        while (!q.isEmpty()) {
            int size = q.size();
            for (int k = 0; k < size; k++) {
                String x = q.poll();
                if (x.equals(target)) {
                    return cnt;
                }

                for (int i = 0; i < words.length; i++) {
                    if (!words[i].equals("")) {
                        int temp = 0;
                        for (int j = 0; j < words[i].length(); j++) {
                            if (words[i].charAt(j) == x.charAt(j)) {
                                temp++;
                            }
                        }

                        if (temp == words[i].length() - 1) {
                            q.add(words[i]);
                            words[i] = ""; // 해당 단어를 방문한 것으로 표시
                        }
                    }
                }
            }
            cnt++; // 각 레벨에 대해 변환 횟수를 증가
        }
        return 0; // 변환 순서가 찾아지지 않은 경우
    }
}
