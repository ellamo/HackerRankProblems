package HackerRankProblems;

import java.util.*;

public class AVeryBigSum {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		long[] longArr = { 1000000001, 1000000002, 1000000003, 1000000004, 1000000005}; 
		
		System.out.println(aVeryBigSum(longArr));
	} // end main method

	
	
	
	public static long aVeryBigSum(long[] ar) {
		
		return Arrays.stream(ar).sum();
		
	} // end aVeryBigSum method
	
	
} // end AVeryBigSum class
