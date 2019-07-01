package HackerRankProblems;

import java.util.*;

public class CompareTheTriplets {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		List<Integer> alice = Arrays.asList(17, 28, 30);
		List<Integer> bob = Arrays.asList(99, 16, 8);
		
		
		List<Integer> score = compareTheTriplets(alice, bob);
		for(Integer el : score) {
			System.out.println(el);
		}
		
		
	} // end main method
	
	
	public static List<Integer> compareTheTriplets(List<Integer> a, List<Integer> b) {
		
		List<Integer> res = Arrays.asList(0, 0);
		
		for(int i = 0; i < a.size(); i++) {
			if ( a.get(i) > b.get(i) ) {
				res.set(0, res.get(0) + 1);
			} else if ( b.get(i) > a.get(i) ) {
				res.set(1, res.get(1) + 1);
			} else {
				continue;
			}
		}
		
		return res;
		
		
		
	} // end calcScores method
	

}  // end CompareTheTriplets class
