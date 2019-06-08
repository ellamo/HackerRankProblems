/*

HackerRank --
Practice > Interview Preparation Kit > Arrays ---> Minimum Swaps 2

*/


import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

   // Complete the minimumSwaps function below.
    static int minimumSwaps(int[] arr) {
        int swapcount = 0;
        int size = arr.length;
        int temp = 0;
        for(int i = 0; i < size; i++) {
            if (arr[i] != i + 1) {
                for(int j = i; j < size; j++) {
                    if (arr[j] == i + 1) {
                        temp = arr[i];
                        arr[i] = arr[j];
                        arr[j] = temp;
                        swapcount++;
                        break;
                    } // end inner condition
                } // end inner loop
            } // end outer condition
        } // end outer loop
        return swapcount;
    } // end minimumSwaps()

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] arr = new int[n];

        String[] arrItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int arrItem = Integer.parseInt(arrItems[i]);
            arr[i] = arrItem;
        }

        int res = minimumSwaps(arr);

        bufferedWriter.write(String.valueOf(res));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
