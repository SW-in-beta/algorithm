/*
모든 달은 28일까지.
약관만큼 더하고, 오늘 날짜보다 작으면 파기
*/
import java.util.*;

class Solution {
    private int daysPerMonth = 28;
    private int daysPerYear = 28 * 12;
    private int[] days = {daysPerYear, daysPerMonth, 1};
    
    public int[] solution(String today, String[] terms, String[] privacies) {
        
        int intToday = dateToInt(today);
        Map<String, Integer> term = new HashMap<>();
        
        for (String t : terms) {
            String[] splitedT = t.split(" ");
            term.put(splitedT[0], Integer.parseInt(splitedT[1]) * daysPerMonth);
        }
        
        List<Integer> expired = new ArrayList<>();
        
        for (int i = 0; i < privacies.length; i++) {
            String privacy = privacies[i];
            String[] splitedPrivacy = privacy.split(" ");
            
            int intDate = dateToInt(splitedPrivacy[0]) + term.get(splitedPrivacy[1]);
            if (intDate <= intToday) {
                expired.add(i + 1);
            }
        }
        
        int[] arr = new int[expired.size()];
        
        for (int i = 0; i < expired.size(); i++) {
            arr[i] = expired.get(i);
        }
        return arr;
    }
    
    public int dateToInt(String date) {
        String[] splitedDate = date.split("\\.");
        int intDate = 0;

        for (int i = 0; i < 3; i++) {
            intDate += (days[i] % 2000) * Integer.parseInt(splitedDate[i]);
        }

        return intDate;
    }
}