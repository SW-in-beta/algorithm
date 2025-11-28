import java.util.*;
import java.util.stream.Collectors;

class Solution {

    static class Emoticon {
        int price;
        int discount;

        Emoticon(int price, int discount) {
            this.price = price;
            this.discount = discount;
        }

        int getDiscountedPrice() {
            return price * (100 - discount) / 100;
        }
    }

    private static final int[] PERCENTS = {10, 20, 30, 40};

    public int[] solution(int[][] users, int[] emoticons) {
        int n = emoticons.length;
        List<List<Integer>> discountCases = generateDiscountCases(n);

        int maxPlus = 0;
        int maxTotal = 0;

        for (List<Integer> discountCase : discountCases) {
            List<Emoticon> emoticonCase = new ArrayList<>();
            
            for (int i = 0; i < n; i++) {
                emoticonCase.add(new Emoticon(emoticons[i], discountCase.get(i)));
            }
            
            int plus = 0;
            int total = 0;
            
            for (int[] user : users) {
                int userTotal = 0;
                int minDiscount = user[0];
                int thresholdTotal = user[1];
                
                for (Emoticon emoticon : emoticonCase) {
                    if (emoticon.discount >= minDiscount) userTotal += emoticon.getDiscountedPrice();
                }
                
                if (userTotal >= thresholdTotal) {
                    plus += 1;
                    continue;
                } else {
                    total += userTotal;
                }
            }
            
            if (plus > maxPlus) {
                maxPlus = plus;
                maxTotal = total;
            } else if (plus == maxPlus) {
                maxTotal = Math.max(maxTotal, total);
            }
        }
        
        return new int[]{maxPlus, maxTotal};
    }

    private static List<List<Integer>> generateDiscountCases(int n) {
        List<List<Integer>> discountCases = Arrays.stream(PERCENTS)
                .boxed()
                .map(List::of)
                .collect(Collectors.toList());

        for (int i = 1; i < n; i++) {
            List<List<Integer>> currentCases = new ArrayList<>();

            for (List<Integer> discountCase : discountCases) {
                for (int p : PERCENTS) {
                    List<Integer> copiedCase = new ArrayList<>(discountCase);
                    copiedCase.add(p);
                    currentCases.add(copiedCase);
                }
            }
            discountCases = currentCases;
        }
        return discountCases;
    }
}