import java.math.BigInteger;
class Solution {
    public String solution(String a, String b) {
        String answer = "";
        BigInteger na = new BigInteger(a);
        BigInteger nb = new BigInteger(b);
        BigInteger result = plus(na, nb);
        answer = result.toString();
        return answer;
    }
    private static BigInteger plus(BigInteger a, BigInteger b) {
        return a.add(b);
    }
}