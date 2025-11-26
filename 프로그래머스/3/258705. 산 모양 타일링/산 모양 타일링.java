class Case {
    public int pCount;
    public int uCount;
    
    public Case() {
        this.pCount = 0;
        this.uCount = 0;
    }
    
    public int getTotal() {
        return this.pCount + this.uCount;
    }
}

class Solution {
    public int solution(int n, int[] tops) {
        Case[] cases = new Case[n];
        for (int i = 0; i < n; i++) {
            cases[i] = new Case();
        }
        
        cases[0].pCount = 1;
        cases[0].uCount = 2 + tops[0];
        
        for (int i = 1; i < n; i++) {
            append(i, cases, tops);
        }
         
        return cases[n-1].getTotal() % 10007;
    }
    
    public void append(int i, Case[] cases, int[] tops) {
        Case priorCase = cases[i-1];
        Case thisCase = cases[i];
        
        thisCase.pCount = priorCase.getTotal() % 10007;
        thisCase.uCount = (priorCase.getTotal() * (1 + tops[i]) + priorCase.uCount) % 10007;
    }
}
