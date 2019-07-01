package HackerRankProblems;

import java.util.*;
import java.util.stream.IntStream;

public class PlusMinus {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = {-4, 3, -9, 0, 4, 1};
		
		plusMinus(nums);
		
	}  // end main method

	
	
	public static void plusMinus(int[] arr) {
	
		int[] counts = new int[3];
		// positive
		counts[0] = Arrays.stream(arr).filter(b -> b > 0).toArray().length;
		// negative
		counts[1] = Arrays.stream(arr).filter(b -> b < 0).toArray().length;
		// zero
		counts[2] = Arrays.stream(arr).filter(b -> b == 0).toArray().length;
		
		for(int i : counts) {
			System.out.format("%.6f\n", (double) i / arr.length );
		}
		
		
	}  // end plusMinus method
	
	
	
	
	
	public static void plusMinusTestMethod(int[] arr) {
		
		// using a stream to filter and printing to ensure it collects properly
		int[] pos = Arrays.stream(arr).filter(b -> b > 0).toArray();
		Arrays.stream(pos).forEach(System.out::println);
		System.out.println("there are " + pos.length + " positive integers");
		// compounding the stream to a single integer count of items and printing to verify
		// this works, so I'll just use this in the actual method
		int posCount = Arrays.stream(arr).filter(b -> b > 0).toArray().length;
		System.out.println("that's a count of " + posCount);
		
		// checking the array of negative numbers
		int[] neg = Arrays.stream(arr).filter(b -> b < 0).toArray();
		System.out.println();
		Arrays.stream(neg).forEach(System.out::println);
		System.out.println("there are " + neg.length + " positive integers");
		
		// checking the array of zeros
		int[] zero = Arrays.stream(arr).filter(b -> b == 0).toArray();
		System.out.println();
		Arrays.stream(zero).forEach(System.out::println);
		System.out.println("there are " + zero.length + " positive integers");
		
		
	}  // end plusMinusTestMethod method
	
	
	
	
}  // end PlusMinus class
