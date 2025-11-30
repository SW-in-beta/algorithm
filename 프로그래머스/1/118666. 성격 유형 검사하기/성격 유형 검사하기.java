/*
MBTI 느낌
같으면 사전 순으로 빠른 성격 유형
*/

import java.util.Map;
import java.util.Arrays;
import java.util.stream.Collectors;

class Solution {
    public String solution(String[] survey, int[] choices) {
        String typeString = "RTCFJMAN";
        Map<String, Integer> scoreMap = Arrays.stream(typeString.split("")).collect(Collectors.toMap(k -> k, k -> 0));
        
        for (int i = 0; i < survey.length; i++) {
            String[] types = survey[i].split("");
            int choice = choices[i];
            int score = 4 - choice;
            int idx = (score > 0) ? 0 : 1;
            scoreMap.put(types[idx], scoreMap.get(types[idx]) + Math.abs(score));
        }
        
        String answer = "";
        for (int i = 0; i < 4; i++) {
            String target1 = String.valueOf(typeString.charAt(i * 2));
            String target2 = String.valueOf(typeString.charAt(i * 2 + 1));
            int score1 = scoreMap.get(target1);
            int score2 = scoreMap.get(target2);
            
            if (score1 > score2) {
                answer += target1;
            } else if (score2 > score1) {
                answer += target2;
            } else {
                answer += target1.compareTo(target2) == 1 ? target2 : target1;
            }
        }
        
        return answer;
    }
}