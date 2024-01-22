import java.util.*;

class Solution {
    public String[] solution(String[][] tickets) {
        List<String> result = new ArrayList<>();
        boolean[] isVisited = new boolean[tickets.length];

        Deque<TravelState> stack = new ArrayDeque<>();
        stack.push(new TravelState("ICN", "ICN", 0));

        while (!stack.isEmpty()) {
            TravelState current = stack.pop();
            int level = current.level;
            String departure = current.departure;
            String path = current.path;

            if (level == tickets.length) {
                result.add(path);
                continue;
            }

            for (int i = 0; i < tickets.length; i++) {
                if (isVisited[i]) continue;

                if (tickets[i][0].equals(departure)) {
                    isVisited[i] = true;
                    stack.push(new TravelState(tickets[i][1], path + " " + tickets[i][1], level + 1));
                    isVisited[i] = false;
                }
            }
        }

        Collections.sort(result);
        return result.get(0).split(" ");
    }

    private static class TravelState {
        String departure;
        String path;
        int level;

        public TravelState(String departure, String path, int level) {
            this.departure = departure;
            this.path = path;
            this.level = level;
        }
    }
}
