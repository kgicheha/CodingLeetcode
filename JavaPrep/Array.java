
import java.util.*;

public class Array {

    public static void main(String[] args) {
        int[] testingArray = new int[5];
        testingArray[0] = 3;
        testingArray[1] = 2;
        testingArray[2] = 210;
        testingArray[3] = 1;

        System.out.println(Arrays.toString(testingArray));
        Arrays.sort(testingArray);
        System.out.println(Arrays.toString(testingArray));
    }
}
