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

    /*
     * Complete the 'countApplesAndOranges' function below.
     *
     * The function accepts following parameters:
     * 1. INTEGER s
     * 2. INTEGER t
     * 3. INTEGER a
     * 4. INTEGER b
     * 5. INTEGER_ARRAY apples
     * 6. INTEGER_ARRAY oranges
     */

    public static void countApplesAndOranges(int s, int t, int a, int b, List<Integer> apples, List<Integer> oranges) {
    
        // Count apples
        int appleCount = 0;
        for (int i = 0; i < apples.size(); i++) {
            int applePosition = a + apples.get(i);
            if (applePosition >= s && applePosition <= t) {
                appleCount++;
            }
        }

        // Count oranges
        int orangeCount = 0;
        for (int i = 0; i < oranges.size(); i++) {
            int orangePosition = b + oranges.get(i);
            if (orangePosition >= s && orangePosition <= t) {
                orangeCount++;
            }
        }

        System.out.println(appleCount + "\n" + orangeCount);
    }
}