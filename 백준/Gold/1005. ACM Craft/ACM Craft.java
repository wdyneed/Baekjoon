import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt(); // 테스트 케이스 개수

        while (T-- > 0) {
            int N = scanner.nextInt(); // 건물 개수
            int K = scanner.nextInt(); // 건설 순서 규칙 개수

            int[] time = new int[N + 1]; // 각 건물의 건설 시간
            int[] indegree = new int[N + 1]; // 각 건물의 진입 차수
            int[] dp = new int[N + 1]; // 각 건물까지의 최소 건설 시간

            ArrayList<ArrayList<Integer>> graph = new ArrayList<>(); // 건설 순서 규칙 그래프
            for (int i = 0; i <= N; i++) {
                graph.add(new ArrayList<>());
            }

            // 건물별 건설 시간 입력
            for (int i = 1; i <= N; i++) {
                time[i] = scanner.nextInt();
            }

            // 건설 순서 규칙 입력 및 그래프 구성
            for (int i = 0; i < K; i++) {
                int X = scanner.nextInt();
                int Y = scanner.nextInt();
                graph.get(X).add(Y);
                indegree[Y]++;
            }

            int target = scanner.nextInt(); // 목표 건물

            // 위상 정렬을 이용한 DP 계산
            Queue<Integer> queue = new LinkedList<>();
            for (int i = 1; i <= N; i++) {
                if (indegree[i] == 0) {
                    queue.offer(i);
                    dp[i] = time[i];
                }
            }

            while (!queue.isEmpty()) {
                int cur = queue.poll();

                for (int next : graph.get(cur)) {
                    dp[next] = Math.max(dp[next], dp[cur] + time[next]);
                    indegree[next]--;

                    if (indegree[next] == 0) {
                        queue.offer(next);
                    }
                }
            }

            System.out.println(dp[target]);
        }
    }
}
