package com.google.challenges; 
import java.math.BigInteger;
public class Answer {   
    public static int answer(String n) { 

        // Your code goes here.
    int c = 0;
        BigInteger int_n = new BigInteger(n);

        while (!(int_n.equals(BigInteger.ONE))) {

                BigInteger three = new BigInteger("3");
                BigInteger plus = int_n.add(BigInteger.ONE);
                BigInteger minus = int_n.subtract(BigInteger.ONE);
//System.out.println("---------");
//System.out.println("plus:"+plus.toString());
//System.out.println("minus:"+minus.toString());
                int p = plus.bitCount();
                int m = minus.bitCount();
                BigInteger tmp = int_n.and(BigInteger.ONE);
//System.out.println("and:"+tmp.toString());
//System.out.println("plus.bitCount:"+p);
//System.out.println("minus.bitCount:"+m);

                if ( tmp.equals(BigInteger.ZERO) ) {

                        int_n = int_n.shiftRight(1);
//System.out.println("int_n.shiftRight:"+int_n);
// int_n >>>= 1;
                } else if (int_n.equals(three) || p > m) {
                        int_n = minus;
                } else {
                        int_n = plus;
                }
                ++c;
        }
        return c;
    } 
}