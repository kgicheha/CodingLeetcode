import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {


    public static int factorial(int n) {
    // Write your code here
       if (n == 0){
           return 1;
       } else{
           return n * factorial(n-1);
       }

    }

}
