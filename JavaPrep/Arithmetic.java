import java.math.*;
import java.text.*;
public class Arithmetic{

    public static void main(String[] args) {
        double result =  (double)10 % (double)3;
        double result2 =  10 % 3;
        int int1 = 1;

        int1++;
        int1++;
        System.out.println("You result is: " + result);
        System.out.println("You result is: " + result2);
        System.out.println(int1);

       int int2 = (int)Math.ceil( 11 / 3);
       System.out.println("result: " + int2);

    //    MAX

       int result3= Math.max(1,2);
       System.out.println(result3);

       int result4 = (int)(Math.random() * 100);
       System.out.println(result4);

       NumberFormat currency = NumberFormat.getCurrencyInstance();
       String result5 = currency.format(1000000.891);
       System.out.println(result5);


    }
}