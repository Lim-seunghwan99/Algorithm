import java.util.PriorityQueue;

class Solution {
    public long solution(int n, int[] works) {
        long answer = 0;

        // Max Heap으로 정렬된 우선순위 큐
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);

        // 우선순위 큐에 works 배열 값 추가
        for (int work : works) {
            maxHeap.offer(work);
        }

        // n 시간 동안 최댓값을 하나씩 감소시키며 피로도 최소화
        while (n > 0 && !maxHeap.isEmpty()) {
            int max = maxHeap.poll();
            if (max > 0) {
                maxHeap.offer(max - 1);
            }
            n--;
        }

        // 남은 작업의 제곱을 더함
        while (!maxHeap.isEmpty()) {
            int work = maxHeap.poll();
            answer += (long) Math.pow(work, 2);
        }

        return answer;
    }
}

// n시간 동안 피로도를 최소화 하도록 일한다.
// -> n시간 동안 일한 뒤에 works의 각 값의 제곱의 합이 최소
// -> 편차를 최대한 작게 하면된다.