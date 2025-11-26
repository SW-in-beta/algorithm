import java.util.*;

class Solution {

    public int solution(String[] friends, String[] gifts) {    
        int n = friends.length;

        // 이름 → index 매핑
        Map<String, Integer> indexMap = new HashMap<>();
        for (int i = 0; i < n; i++) {
            indexMap.put(friends[i], i);
        }

        // 선물 기록 및 선물 지수
        int[][] giftMatrix = new int[n][n];
        int[] giftScore = new int[n];

        // 기록 채우기
        for (String gift : gifts) {
            String[] parts = gift.split(" ");
            int sender = indexMap.get(parts[0]);
            int receiver = indexMap.get(parts[1]);

            giftMatrix[sender][receiver] += 1;
            giftScore[sender] += 1;
            giftScore[receiver] -= 1;
        }

        // 각 사람의 다음 달 선물 개수 계산
        int maxCount = 0;
        for (int i = 0; i < n; i++) {
            int count = countGifts(i, giftMatrix, giftScore);
            maxCount = Math.max(maxCount, count);
        }

        return maxCount;
    }

    /** i번 사람이 다음 달에 받는 선물 수 계산 */
    private int countGifts(int me, int[][] giftMatrix, int[] giftScore) {
        int n = giftMatrix.length;
        int result = 0;

        for (int other = 0; other < n; other++) {
            if (me == other) continue;

            int sent = giftMatrix[me][other];
            int received = giftMatrix[other][me];

            if (sent > received) {
                result++;
            } else if (sent == received) {
                if (giftScore[me] > giftScore[other]) {
                    result++;
                }
            }
        }

        return result;
    }
}