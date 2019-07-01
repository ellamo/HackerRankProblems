package HackerRankProblems;

public class Staircase {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		int stairs = 3;
	
		staircase(stairs);
		
		
	}  // end main method

	
	
	public static void staircase(int n) {
		
		int x = 1;
		while (x < n + 1) {
			for(int i = n - x; i > 0; i--) {
				System.out.print(" ");
			}
			for(int i = x; i > 0; i--) {
				System.out.print("#");
			}
			if(n - x != 0) {
				System.out.println();
			}
			x++;
		}
		
		//System.out.println("the end");
		
	} // end staircase method
	
	
	
	
	
	
	
}  // end Staircase class
