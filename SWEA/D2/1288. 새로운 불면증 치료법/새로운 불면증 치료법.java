import java.util.*;
import java.io.*;

class Solution
{
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        for(int T=1; T<=t; T++){
            int N = Integer.parseInt(br.readLine());

            boolean[] num = new boolean[10];
            int count = 0;  
            int find = 0;  

            while(true){
                long numstR = N*(count+1);

                while(numstR > 0){
                    int rmn = (int)numstR%10;
                    if(!num[rmn]){
                        num[rmn] = true;
                        find++;
                    }
                    numstR /= 10;
                }
                count++;
                if(find==10){
                    break;
                }
            } 
            System.out.println("#"+T + " "+(N * count));
        }
    }
}
