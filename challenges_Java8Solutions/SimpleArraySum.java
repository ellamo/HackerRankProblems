package HackerRankProblems;

import java.util.*;

public class SimpleArraySum {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		List<Integer> nums = Arrays.asList(1, 2, 3);
		
		forEachSolution(nums);
		streamListSolution(nums);
		
		
		int[] ar = {1, 2, 3};
		List nums2 = Arrays.asList(nums);	
		//streamSolution(nums2);     // problematic casting issue
		
		streamIntArraySolution(ar);
		
		
	} // end main method
	
	
	
	public static int streamIntArraySolution(int[] arr) {
		
		int sum = Arrays.stream(arr).reduce(0, Integer::sum);
		System.out.println("streamIntArraySolution: " + sum);
		return sum;
		
	} // end streamIntArraySolution method
	

	
	public static int streamListSolution(List<Integer> arr) {
		
		int sum = arr.stream().reduce(0, Integer::sum);
		System.out.println("streamSolution: " + sum);
		return sum;
		
	} // end streamSolution method
	
	
	
	public static int forEachSolution(List<Integer> arr) {
		int sum = 0;
		for(int x : arr) {
			sum += x;
		}
		
		System.out.println("forEachSolution: " + sum);
		return sum;
		
	} // end forEachSolution method
	
	
} // end SimpleArraySum class
